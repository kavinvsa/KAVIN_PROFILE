from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from resume_knowledge import RESUME_DOCUMENTS, corpus_texts

app = FastAPI(
    title="Ask Me Chatbot",
    description="A small chatbot backend that answers questions from Kavin.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, description="Question about the resume")
    top_k: int = Field(4, ge=1, le=8, description="Number of matching resume chunks to return")


class SourceChunk(BaseModel):
    title: str
    section: str
    score: float
    content: str


class ChatResponse(BaseModel):
    answer: str
    confidence: float
    sources: list[SourceChunk]


@dataclass
class RetrievalHit:
    title: str
    section: str
    score: float
    content: str


class ResumeRAG:
    def __init__(self) -> None:
        self.documents = RESUME_DOCUMENTS
        self.texts = corpus_texts()
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(self.texts)

    def retrieve(self, question: str, top_k: int = 4) -> list[RetrievalHit]:
        query_vector = self.vectorizer.transform([question])
        scores = cosine_similarity(query_vector, self.matrix).ravel()
        ranked_indexes = scores.argsort()[::-1][:top_k]

        hits: list[RetrievalHit] = []
        for index in ranked_indexes:
            doc = self.documents[index]
            hits.append(
                RetrievalHit(
                    title=doc["title"],
                    section=doc["section"],
                    score=float(scores[index]),
                    content=doc["content"],
                )
            )
        return hits

    @staticmethod
    def _format_project_list(docs: list[dict[str, Any]]) -> str:
        project_titles = [doc["title"] for doc in docs if doc["section"] == "projects"]
        return ", ".join(project_titles)

    @staticmethod
    def _format_experience_list(docs: list[dict[str, Any]]) -> str:
        experience_titles = [doc["title"] for doc in docs if doc["section"] == "experience"]
        return "; ".join(experience_titles)

    def answer(self, question: str, top_k: int = 4) -> ChatResponse:
        hits = self.retrieve(question, top_k=top_k)
        best_score = hits[0].score if hits else 0.0

        q = question.lower()
        if any(term in q for term in ["project", "projects", "work"]):
            project_titles = self._format_project_list(self.documents)
            answer = (
                "Your resume includes these projects: "
                f"{project_titles}. I can also share details about any one of them if you ask for it."
            )
        elif any(term in q for term in ["skill", "skills", "tools", "tech stack", "technologies"]):
            answer = (
                "Your resume highlights Python, SQL, JavaScript, LangChain, LangGraph, RAG, Agentic AI, "
                "PyTorch, TensorFlow, Azure AI, AWS Bedrock, OpenSearch, Milvus, Neo4j, FastAPI, Docker, and Power BI."
            )
        elif any(term in q for term in ["experience", "worked", "company", "role"]):
            experience_titles = self._format_experience_list(self.documents)
            answer = (
                "Your experience includes: "
                f"{experience_titles}. Ask me about any one role for a deeper summary."
            )
        else:
            if best_score < 0.05:
                answer = (
                    "I could not find a strong match in your resume for that question. "
                    "Try asking about your projects, experience, skills, tools, or achievements."
                )
            else:
                top_lines = []
                for hit in hits[:3]:
                    top_lines.append(f"{hit.title}: {hit.content}")
                answer = "Based on your resume, " + " ".join(top_lines)

        confidence = round(min(1.0, best_score if best_score > 0 else 0.2), 3)
        sources = [
            SourceChunk(
                title=hit.title,
                section=hit.section,
                score=round(hit.score, 4),
                content=hit.content,
            )
            for hit in hits
        ]
        return ChatResponse(answer=answer, confidence=confidence, sources=sources)


@lru_cache(maxsize=1)
def get_engine() -> ResumeRAG:
    return ResumeRAG()


@app.get("/", summary="Root")
def root() -> dict[str, str]:
    return {
        "name": "Ask Me",
        "status": "ready",
        "message": "Use POST /chat to ask questions about Kavin.",
    }


@app.get("/health", summary="Health check")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse, summary="Ask Me Chatbot")
def chat(payload: ChatRequest) -> ChatResponse:
    engine = get_engine()
    return engine.answer(payload.question, top_k=payload.top_k)

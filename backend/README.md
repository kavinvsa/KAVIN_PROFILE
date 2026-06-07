# Resume RAG Chatbot Backend

A small FastAPI backend that answers questions from Kavin S's resume using a retrieval step over embedded resume content.

## Features
- Answers questions about projects, skills, tools, and experience.
- Uses TF-IDF retrieval to find the most relevant resume sections.
- Returns the answer plus source chunks for transparency.
- Enables CORS for easy frontend integration.

## Endpoints
- `GET /` - service status
- `GET /health` - health check
- `POST /chat` - ask a question about the resume

### Example request
```json
{
  "question": "What projects have you worked on?",
  "top_k": 4
}
```

### Example response
```json
{
  "answer": "Your resume includes these projects: ...",
  "confidence": 0.91,
  "sources": []
}
```

## Run locally
1. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```
2. Start the server:
   ```bash
   uvicorn app:app --reload --port 8000
   ```
3. Open:
   - `http://localhost:8000/docs`

## Notes
- The resume knowledge base is stored in `resume_knowledge.py`.
- If you want to connect this backend to your frontend later, call `POST /chat` from JavaScript.

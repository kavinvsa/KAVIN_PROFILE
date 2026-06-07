"""Resume knowledge base for the backend RAG chatbot."""

from __future__ import annotations

RESUME_DOCUMENTS = [
    {
        "id": "summary",
        "section": "summary",
        "title": "Professional Summary",
        "content": (
            "Kavin S is an AI Engineer based in Bengaluru, India, focused on Generative AI, "
            "NLP, Agentic AI, enterprise analytics, retrieval augmented generation, and "
            "production-first AI systems that deliver reliable behavior, traceable outputs, "
            "and measurable business value."
        ),
    },
    {
        "id": "core_expertise",
        "section": "skills",
        "title": "Core Expertise",
        "content": (
            "Machine Learning, Deep Learning, Generative AI, RAG, Agentic AI, model evaluation, "
            "and prompt engineering."
        ),
    },
    {
        "id": "programming_skills",
        "section": "skills",
        "title": "Programming Skills",
        "content": "Python, SQL, and JavaScript.",
    },
    {
        "id": "framework_skills",
        "section": "skills",
        "title": "AI Framework Skills",
        "content": "LangChain, LangGraph, RAG systems, Agentic AI, PyTorch, and TensorFlow.",
    },
    {
        "id": "cloud_tools",
        "section": "skills",
        "title": "Cloud and Tools",
        "content": "Azure AI, AWS Bedrock, OpenSearch, Milvus, Neo4j, FastAPI, Docker, and Power BI.",
    },
    {
        "id": "experience_schneider",
        "section": "experience",
        "title": "Schneider Electric - AI Engineer",
        "content": (
            "Developed an Agentic AI platform handling Excel, PDF, email, image, and SLD diagram inputs "
            "using Hybrid RAG for evidence-backed responses with confidence scoring."
        ),
    },
    {
        "id": "experience_walmart",
        "section": "experience",
        "title": "Walmart, Bengaluru - Generative AI Specialist and Data Scientist",
        "content": (
            "Improved material selection outcomes by 70 percent through GenAI workflows and built evaluation "
            "systems for fairness, faithfulness, BLEU, F1, and response quality."
        ),
    },
    {
        "id": "experience_kpmg",
        "section": "experience",
        "title": "KPMG India - AI Engineer",
        "content": (
            "Built Buddy Agent to guide users through applications with contextual assistance and improved feature adoption "
            "using Milvus, Neo4j, and Azure App Services."
        ),
    },
    {
        "id": "experience_tcs",
        "section": "experience",
        "title": "Tata Consultancy Services - AI and Data Science Consultant",
        "content": (
            "Designed AI automation and retrieval workflows, including FlowChartGPT and large-document RAG use cases, "
            "improving response speed and decision support."
        ),
    },
    {
        "id": "experience_vhs",
        "section": "experience",
        "title": "VHS Consultancy Services - Data Scientist",
        "content": (
            "Built predictive models for downstream desalter systems, improved issue detection by 8x, and contributed to "
            "projected value of 90 million dollars with operational KPI dashboards."
        ),
    },
    {
        "id": "experience_simtech",
        "section": "experience",
        "title": "SimTech IT Solutions - QA and Data Projects",
        "content": (
            "Worked on quality engineering, crash test variation analytics, and large-document RAG chatbot systems that "
            "improved context-aware response time by 90 percent."
        ),
    },
    {
        "id": "project_order_handover",
        "section": "projects",
        "title": "AI-Powered Order Handover Automation and Knowledge Retrieval Platform",
        "content": (
            "An agentic AI system that processes multi-format data including Excel files, PDFs, images, emails, and SLD diagrams "
            "to generate evidence-backed Yes, No, or Not Available responses with reasoning, source references, and confidence scores. "
            "Tools used include Python, AWS Bedrock with Claude and Titan, OpenSearch vector search, OCR and document parsing, Pandas, "
            "prompt engineering, and workflow automation."
        ),
    },
    {
        "id": "project_evaluation",
        "section": "projects",
        "title": "Multi-Metric AI Evaluation System",
        "content": (
            "An evaluation system for accuracy, efficiency, fairness, faithfulness, ground truth alignment, bias, BLEU, F1 score, "
            "and overall response quality. Tools used include RAGAS, RAG Evals, LangSmith, and GenAI evaluators."
        ),
    },
    {
        "id": "project_buddy_agent",
        "section": "projects",
        "title": "Buddy Agent - Intelligent User Assistance System",
        "content": (
            "A Buddy Agent that guides users through the application, helps them understand its features, and simplifies the "
            "overall experience. Tools used include GPT-5.1, Milvus, Neo4j, and Azure App Services."
        ),
    },
    {
        "id": "project_material_selection",
        "section": "projects",
        "title": "Optimized Material Selection with Generative AI",
        "content": (
            "Leveraged Generative AI to streamline material selection during sourcing, improving material performance by 70 percent "
            "while helping reduce costs and improve sustainability metrics. Tools used include LangChain, ChromaDB, and GPT-4o."
        ),
    },
    {
        "id": "project_flowchartgpt",
        "section": "projects",
        "title": "FlowChartGPT - AI-Powered Flowchart Extraction and Chatbot Integration System",
        "content": (
            "An AI-driven chatbot that extracts information from flowcharts, converts it into structured JSON, and integrates with GPT models "
            "to deliver accurate and context-aware responses."
        ),
    },
    {
        "id": "project_large_docs_rag",
        "section": "projects",
        "title": "Chatbot with RAG Model for Large Documents Handling",
        "content": (
            "A Retrieval Augmented Generation model for large documents such as 1000 plus page PDFs, improving query response time by 90 percent "
            "through text retrieval and generative capabilities."
        ),
    },
    {
        "id": "project_hpoint",
        "section": "projects",
        "title": "H-Point Variation Analysis for Enhanced CAE Crash Test Correlation",
        "content": (
            "Analyzed variations in the mean H-point during crash tests, estimated deviations from the design H-point, and improved correlation "
            "between CAE crash simulations and physical test results, enhancing crashworthiness prediction accuracy by 70 percent."
        ),
    },
    {
        "id": "project_desalter",
        "section": "projects",
        "title": "Downstream Desalter Analysis - Predictive Modelling",
        "content": (
            "Built an end-to-end predictive pipeline for one of the largest multi-stage desalter systems in North America, identifying drivers of efficiency, "
            "detecting evaporator problems 8x quicker, and supporting projected business growth valued at 90 million dollars. "
            "Developed interactive Power BI dashboards to visualize KPIs, track desalter efficiency, and monitor operational trends."
        ),
    },
]


def corpus_texts() -> list[str]:
    """Return documents as retrievable text blobs."""
    return [f"{doc['title']}: {doc['content']}" for doc in RESUME_DOCUMENTS]

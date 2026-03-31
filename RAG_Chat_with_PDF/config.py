'''
rag_pdf_bot/
│
├── app.py
├── rag_pipeline.py
└── config.py

Upload PDF
→ System reads PDF
→ Creates embeddings
→ Stores in vector DB
→ User asks question
→ AI answers from PDF

Document → Chunk → Embedding → Vector DB → Retrieval → LLM → Answer

'''
OPENAI_API_KEY = 'api_secret_123456'
MODEL = "gpt-4o-mini"
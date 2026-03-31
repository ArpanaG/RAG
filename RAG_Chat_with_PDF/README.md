# RAG Chat with PDF

A lightweight Streamlit app to ask questions over a PDF using PDF parsing, embeddings, and retrieval-augmented generation (RAG).

## Features

- Upload a PDF via web UI
- Split document into chunks
- Create OpenAI embeddings
- Store vectors in FAISS
- Retrieve and answer questions with OpenAI chat model

## Requirements

- Python 3.10+
- `pip install -r requirements.txt`
- OpenAI API key in `config.py` or environment variable

## Setup

1. Clone project:
   ```bash
   git clone <repo>
   cd RAG_Chat_with_PDF
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set API key in `config.py`:
   ```python
   OPENAI_API_KEY = "your-key"
   MODEL = "gpt-4o-mini"
   ```

## Run

```bash
streamlit run app.py
```

## Usage

1. Open UI at `http://localhost:8501`
2. Upload a PDF file
3. Wait for indexing to complete
4. Enter question and read the answer

## Notes

- Currently uses local FAISS in-memory index; restarted app resets memory.
- `pypdf` is required by `PyPDFLoader`.
- Swap `MODEL` in `config.py` as needed.

## Troubleshooting

- `ImportError`: ensure `pip install -r requirements.txt` succeeded.
- `Streamlit run app: not found`: use `python -m streamlit run app.py`.
- OpenAI quota/error: verify key and subscription.

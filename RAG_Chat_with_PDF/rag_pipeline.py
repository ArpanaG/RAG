from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

from config import OPENAI_API_KEY, MODEL


def build_rag(pdf_path):

    # 1. Load PDF
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # 2. Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)
    print(f"Total chunks created: {len(chunks)}")
    
    # 3. Create embeddings
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

    # 4. Store in FAISS
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    # example retrieval to test
    query = "What is this document about?"
    results = vectorstore.similarity_search(query, k=3)
    for r in results:
        print(r.page_content)

    # 5. LLM
    llm = ChatOpenAI(
        model=MODEL,
        api_key=OPENAI_API_KEY
    )

    '''    We can directly use the RetrievalQA chain, but for demonstration,
    let's see how we can manually create a prompt and get a response from the LLM.
    context = "\n".join([r.page_content for r in results])
    prompt = f"""
    Answer based only on this context:

    {context}

    Question: {query}
    """
    response = llm.invoke(prompt)
    print(response.content)
    '''
    # 6. Retrieval chain (connects retriever + LLM)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa
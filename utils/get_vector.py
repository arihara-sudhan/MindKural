from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="distilbert-base-nli-stsb-mean-tokens")
    vector_store = FAISS.load_local("data/faiss-index", embeddings, allow_dangerous_deserialization=True)
    print(f"VECTOR STORE LOADED < 'faiss-index'")
    return vector_store

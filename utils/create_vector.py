from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from utils.corpus_reader import read_corpus
from utils.text_splitter import split_text

corpus = "\n".join(read_corpus("data/corpus.json"))
texts = split_text(corpus)
embeddings = HuggingFaceEmbeddings(model_name="distilbert-base-nli-stsb-mean-tokens")
vector_store = FAISS.from_texts(texts, embeddings)
vector_store.save_local("data/faiss-index")


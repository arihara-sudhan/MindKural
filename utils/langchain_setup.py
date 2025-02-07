from utils.corpus_reader import read_corpus
from utils.text_splitter import split_text
from utils.get_vector import load_vector_store
from utils.qa_chain_setup import setup_qa_chain

vector_store = load_vector_store()
qa_chain = setup_qa_chain(vector_store)

def get_qa_chain():
    return qa_chain

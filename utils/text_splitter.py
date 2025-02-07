from langchain.text_splitter import CharacterTextSplitter

def split_text(corpus, chunk_size=100, chunk_overlap=10):
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(corpus)

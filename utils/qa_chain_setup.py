import os
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
import utils.config as config

def setup_qa_chain(vector_store):
    #os.environ["HUGGINGFACEHUB_API_TOKEN"] = config.HUGGINGFACEHUB_API_TOKEN

    llm = HuggingFaceHub(
        repo_id="tiiuae/falcon-7b-instruct",
        huggingfacehub_api_token=config.HUGGINGFACEHUB_API_TOKEN
    )

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "Use the following context to answer the question."
            "Answer should be from the exact context, there can be multiple matches. but, answer from the highly matching context. Please include the Number of the highly matched context like Kural: Number. Enrich the answer with simple words. The response should start like, Thirukkural says. If the context doesn't have the answer, please politely say, I can't answer that.'\n\n"
            "Context: {context}\n\n"
            "Question: What does Thirukkural says for the question: {question}\n\n"
            "Answer:"
        )
    )

    retriever = vector_store.as_retriever()
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=retriever,
        combine_docs_chain_kwargs={"prompt": prompt_template}
    )

    return qa_chain

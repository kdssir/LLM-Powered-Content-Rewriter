from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

import os

def create_resume_index(resume_dir: str, api_key: str):
    # Load resume file(s)
    documents = SimpleDirectoryReader(resume_dir).load_data()

    # LLaMA 3 via Groq
    llm = OpenAI(
        api_base="https://api.groq.com/openai/v1",
        api_key=api_key,
        model="llama3-8b-8192",
    )

    index = VectorStoreIndex.from_documents(documents, llm=llm)
    return index

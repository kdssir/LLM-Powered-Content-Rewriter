# For Together.ai 
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os

# Set your Together.ai API key (best via environment variable)
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "tgp_v1_8qKhYCTahA1_HV5ETYkOKwpNZhVLNrkHVrnxUulKg-8")

llm = ChatOpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=TOGETHER_API_KEY,
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0.7
)

# Prompt template
prompt = ChatPromptTemplate.from_template("""
You are a professional writing assistant.

Rewrite the following {type} to sound more {tone}:

"{text}"

Rewritten version:
""")

def rewrite_text(text: str, tone: str, type_: str) -> str:
    formatted_prompt = prompt.format_messages(text=text, tone=tone, type=type_)
    return llm.invoke(formatted_prompt).content

def rewrite_with_resume_context(text, tone, type_, index):
    query_engine = index.as_query_engine()
    context = query_engine.query("Summarize the tone and style of this resume.")
    
    full_prompt = f"""
Resume Style: {context}

Now, rewrite the following {type_} to sound more {tone} and aligned with the resume style:

{text}
"""
    return llm.invoke(full_prompt)

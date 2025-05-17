from langchain_core.prompts import PromptTemplate

rewriter_prompt = PromptTemplate.from_template("""
Rewrite the following {type} to sound more {tone}:

"{text}"

Rewritten Version:
""")

from fastapi import FastAPI
from backend.llm import llm
from backend.prompts import rewriter_prompt
from backend.models import RewriteRequest

app = FastAPI()

@app.post("/rewrite")
def rewrite_text(req: RewriteRequest):
    prompt = rewriter_prompt.format(text=req.text, tone=req.tone, type=req.type)
    rewritten = llm.invoke(prompt)
    return {"rewritten": rewritten}

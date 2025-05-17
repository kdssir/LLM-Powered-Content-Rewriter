from pydantic import BaseModel

class RewriteRequest(BaseModel):
    text: str
    tone: str
    type: str  # 'email' or 'resume'

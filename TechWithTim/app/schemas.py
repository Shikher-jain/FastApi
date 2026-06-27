from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str | None = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str | None = None
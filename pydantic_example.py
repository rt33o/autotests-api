from pydantic import BaseModel

class user(BaseModel):
    id: int
    name: str
    email: str

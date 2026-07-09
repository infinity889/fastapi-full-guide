from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int | None = None


@app.get("/{user_id}")
async def read_root(user_id: int):
    return {"user_id": user_id}

@app.post("/")
async def post_root(users: list[User] | None = None):
    if users is None or len(users) == 0:
        return {"names": "b"}
    
    names = [user.name for user in users]
    return {"names": f"hello {', '.join(names)}"}
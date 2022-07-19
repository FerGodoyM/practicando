from pydoc import describe
from typing import Optional
from uuid import uuid4 as uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr


app = FastAPI(title="practicando",
            description="Practicando FastApi, pydantic y peewe",
            version="1.0.1")

Users = []

class user_model(BaseModel):
    id: Optional[str]
    username: str
    password: str
    email: EmailStr

@app.get("/")
async def hola():
    return {"message":"hola mundo"}

@app.get("/users")
async def get_users():
    return Users


@app.post("/users")
async def save_users(user: user_model):
    user.id = str(uuid())
    Users.append(user.dict())
    return Users[-1]

@app.get("/users/{id_users}")
async def id_users(id_users : str):
    for user in Users:
        if user["id"] == id_users:
            return user
    return HTTPException(status_code=404, detail="user not found")
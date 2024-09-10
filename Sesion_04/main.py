from fastapi import FastAPI, status, Depends
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from sqlalchemy.orm import Session
from app.v1.model.model import User
from app.v1.utils.db import engine, get_db
from app.v1.schema.user_schemas import UserRequest, UserResponse


# instanciamos la clase FastAPI
app = FastAPI()
# Creamos nuestro primer modelo


class Post(BaseModel):
    author: str
    title: str
    content: str


class Role(str, Enum):
    admin = "admin"
    user = "user"


class UserA(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    city: str
    roles: List[Role]


@app.get("/")
async def root():
    return {"name": "Anthony Carrillo"}


@app.get("/posts/{id}")
async def getPost(id):
    return {"data": id}


@app.post('/posts')
async def viewPost(post: Post):
    return {"alert": f"El post de {post.title} ha sido agregado a la biblicoteca"}


@app.post("/api/v1/add_user")
async def create_user(user: UserA):
    db.append(user)
    return {"id": user.id}


@app.get("/api/v1/users")
def get_all_users():
    return db


@app.delete("/api/v1/users/{id}")
def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return


@app.get('/all_users', status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    all_users = db.query(User).all()
    return all_users


@app.post('/new_user', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_new_user(post_user: UserRequest, db: Session = Depends(get_db)):
    #new_user = User(username=user.username, email=user.email)
    new_user = User(**post_user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.__dict__


# @app.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
# def create_user(post_user: UserRequest, db: Session = Depends(get_db)):
#     new_user = User(**post_user.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user.__dict__


db: List[UserA] = [
    UserA(
        id=uuid4(),
        first_name="Freddy",
        last_name="Nolaszo",
        city="Lima",
        roles=[Role.user]
    ),
    UserA(
        id=uuid4(),
        first_name="Juan",
        last_name="Falcón",
        city="Trujillo",
        roles=[Role.admin]
    ),
    UserA(
        id=uuid4(),
        first_name="Noelia",
        last_name="Perez",
        city="Lima",
        roles=[Role.user]
    ),
    UserA(
        id=uuid4(),
        first_name="Edwin",
        last_name="Deza",
        city="Cusco",
        roles=[Role.user, Role.admin]
    ),
]

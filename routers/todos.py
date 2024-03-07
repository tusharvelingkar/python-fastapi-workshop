from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from starlette import status
from models import Todos
from database import SessionLocal

router = APIRouter(tags=["Todos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class TodoRequest(BaseModel):
    title: str
    description: str
    priority: int
    complete: bool


@router.get("/todos", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict())

    db.add(todo_model)
    db.commit()

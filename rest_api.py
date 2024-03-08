from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Define a pydantic model for the Book
class Book(BaseModel):
    id: int
    title: str
    author: str


# Mock data for books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

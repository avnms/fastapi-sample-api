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


# Endpoint to get all books
@app.get("/books")
def get_books():
    return books


# Run the app using Uvicorn server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", port=8000)

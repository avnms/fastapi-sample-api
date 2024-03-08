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


# Endpoint to get details of a specific book
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# Endpoint to add a new book
@app.post("/books")
def add_book(book: Book):
    books.append(book.model_dump())
    return book


# Endpoint to update an existing book
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            books[i] = book.model_dump()
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# Endpoint to delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            del books[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")


# Run the app using Uvicorn server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("rest_api:app", host="0.0.0.0", port=8000, reload=True)

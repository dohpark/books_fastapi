from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# 책 정보 모델 정의
class Book(BaseModel):
    title: str
    author: str
    category: str
    description: Optional[str] = None

# 임시 데이터베이스
books_db = []

# 책 정보 생성
@app.post("/books", response_model=Book)
def create_book(book: Book):
    books_db.append(book)
    return book

# 책 목록 가져오기
@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

# 책 정보 읽기 
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    return books_db[book_id]

# 책 정보 갱신하기
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    books_db[book_id] = updated_book
    return updated_book

# 책 정보 삭제하기
@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    deleted_book = books_db.pop(book_id)
    return deleted_book
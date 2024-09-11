from pydantic import BaseModel

from db.models import BookType


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    genre: str
    title: str
    description: str
    price: int
    book_type: BookType


class BookCreate(BookBase):
    author_id: int


class Book(BookBase):
    id: int
    book_type: BookType

    class Config:
        orm_mode = True

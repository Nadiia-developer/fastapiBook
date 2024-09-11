from enum import StrEnum, auto

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship


from db.engine import Base


class BookType(StrEnum):
    Disk = auto()
    E_Book = auto()


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    genre = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(511), nullable=False)
    price = Column(Integer, nullable=False)
    book_type = Column(Enum(BookType), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship(Author)

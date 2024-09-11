from sqlalchemy.orm import Session
from db import models
import schemas
from db.models import BookType, Author


def get_all_authors(db: Session):
    return db.query(models.Author).all()


def get_author_name(db: Session, name: str):
    return (
        db.query(models.Author).filter(models.Author.name == name).first()
    )


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
        name=author.name,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def get_book_list(
        db: Session,
        book_type: BookType | None = None,
        author: str | None = None,
):
    queryset = db.query(models.Book)

    if book_type is not None:
        queryset = queryset.filter(models.Book.book_type == book_type.value)
    if author is not None:
        queryset = queryset.filter(models.Book.author.has(name=author))

    return queryset.all()


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        genre=book.genre,
        title=book.title,
        description=book.description,
        price=book.price,
        book_type=book.book_type,
        author_id=book.author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book

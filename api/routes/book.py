from pydantic import BaseModel


class BookModel(BaseModel):
    author: str
    title: str
    about_book: str
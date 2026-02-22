import sqlalchemy
from .db_session import *
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Session = get_session()
Base = declarative_base()


class BookShem(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str]
    title: Mapped[str]
    about_book: Mapped[str]

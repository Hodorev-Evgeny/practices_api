import uvicorn
from fastapi import FastAPI, HTTPException
from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError

from models.book import BookShem
from routes.book import BookModel
from deps import *


app = FastAPI()


@app.post("/add_book", tags=["book"], summary="Add new book")
async def add_book(session: SessionDep, book: BookModel):
    try:
        new_book = BookShem(author=book.author, title=book.title, about_book=book.about_book)
        session.add(new_book)
        await session.commit()
        return {'status': 'success', 'message': 'Book added successfully!'}

    except IndentationError as e:
        return HTTPException(status_code=400, detail=f"This book already exists! {e}")

    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=f"Error with database: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@app.get("/get_book", tags=["book"], summary="Get book")
async def get_book(session: SessionDep, pagination: PaginationParmsDep):
    try:
        query = select(BookShem).limit(pagination.limit).offset(pagination.offset)
        result = await session.execute(query)
        respouns = result.scalars().all()
        return respouns
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_book", tags=["book"], summary="Update book")
async def update_book(id: int, session: SessionDep, book: BookModel):
    try:
        query = update(BookShem)\
            .where(BookShem.id == id)\
            .values(author=book.author, title=book.title, about_book=book.about_book)
        await session.execute(query)
        await session.commit()
        return {'status': 'success', 'message': 'Book updated successfully!'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_book", tags=["book"], summary="Delete book")
async def delete_book(id: int, session: SessionDep):
    try:
        query = delete(BookShem).where(BookShem.id == id)
        await session.execute(query)
        await session.commit()
        return {'status': 'success', 'message': 'Book deleted successfully!'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app)
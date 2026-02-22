from fastapi import Depends
from typing import Annotated
from models.db_session import get_session
from routes.pagination import PaginationParms
from sqlalchemy.ext.asyncio import AsyncSession


async def session_depends():
    async with Session() as s:
        yield s

Session = get_session()

SessionDep = Annotated[AsyncSession, Depends(session_depends)]
PaginationParmsDep = Annotated[PaginationParms, Depends(PaginationParms)]
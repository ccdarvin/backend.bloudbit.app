from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

import uuid

from .config import settings
from .utils import GUUID

engine = create_async_engine(
    settings.database_url,
    echo=True,
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class UUIDBase(Base):
    __abstract__ = True
    
    id: Mapped[uuid.UUID] = mapped_column(GUUID(), primary_key=True, default=uuid.uuid4)
    


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

    
async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select

DATABASE_URL = "sqlite+aiosqlite:///./products.db" # db connection

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

async def init_db():
    async with engine.begin() as conn:
        # Creates the table if it doesn't already exist
        await conn.run_sync(Base.metadata.create_all)

from sqlalchemy.ext.asyncio import create_async_engine

from config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)



import asyncio
from sqlalchemy import text

async def test():
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))
        print("Database Connected ✅")

asyncio.run(test())

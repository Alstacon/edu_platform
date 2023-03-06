from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import settings

# async engine for interaction with db
engine = create_async_engine(
    settings.REAL_DB_URL,
    future=True,
    echo=True,
)

# create session
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

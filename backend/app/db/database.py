import os
import logging
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from app.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

db_url = settings.DATABASE_URL
# Automatically normalize postgres connection strings from Render / Supabase / Neon
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql+asyncpg://", 1)
elif db_url.startswith("postgresql://") and not db_url.startswith("postgresql+asyncpg://"):
    db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)

connect_args = {"check_same_thread": False, "timeout": 30} if "sqlite" in db_url else {}
engine = create_async_engine(db_url, echo=False, future=True, connect_args=connect_args)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting async database session."""
    async with async_session() as session:
        yield session

async def create_db_and_tables():
    """Create database tables and handle schema migrations."""
    if "sqlite" in db_url:
        os.makedirs("./data", exist_ok=True)
    try:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
            
            # Auto-migrate missing columns for SQLite
            if "sqlite" in db_url:
                try:
                    from sqlalchemy import text
                    await conn.execute(text("ALTER TABLE interviewsession ADD COLUMN proctoring_logs TEXT;"))
                except Exception:
                    pass  # Column already exists
        logger.info("Database tables initialized successfully.")
    except Exception as e:
        logger.warning(f"Database table check warning: {e}")


"""
Configuración de base de datos con SQLModel y asyncpg.
"""

import os
from collections.abc import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

load_dotenv()

# Obtener URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está configurada en el archivo .env")

# Asegurar que usamos el driver asíncrono
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Motor de base de datos
engine = create_async_engine(
    DATABASE_URL,
    poolclass=NullPool,
    future=True,
)

# Factory de sesiones
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependencia para obtener sesión de base de datos."""
    async with async_session_maker() as session:
        yield session


async def init_db():
    """Inicializa la base de datos creando las tablas."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

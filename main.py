"""
Aplicación básica de FastAPI.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.database import init_db
from app.routes import main_router, auth_router, usuarios_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Ciclo de vida de la aplicación."""
    # Inicio: Crear tablas
    await init_db()
    print("✅ Base de datos inicializada")
    yield
    # Fin: Limpieza si fuera necesaria


app = FastAPI(
    title="VOCES API",
    description="API básica con FastAPI + SQLModel",
    version="1.0.0",
    lifespan=lifespan,
)

# Registrar routers
app.include_router(main_router)
app.include_router(auth_router)
app.include_router(usuarios_router)

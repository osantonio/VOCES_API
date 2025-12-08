"""
Rutas - Exportaciones centralizadas.
"""

from app.routes.main import router as main_router
from app.routes.auth import router as auth_router
from app.routes.usuarios import router as usuarios_router

__all__ = [
    "main_router",
    "auth_router",
    "usuarios_router",
]

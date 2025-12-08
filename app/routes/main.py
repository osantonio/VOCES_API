"""
Rutas principales de la aplicación.
"""

from fastapi import APIRouter

router = APIRouter(tags=["General"])


@router.get("/")
async def root():
    """Endpoint raíz."""
    return {
        "mensaje": "Bienvenido a VOCES API",
        "version": "1.0.0",
        "documentacion": "/docs",
    }

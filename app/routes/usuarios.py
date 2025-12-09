"""
Rutas de gestión de usuarios.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.core.database import get_session
from app.core.deps import get_current_user
from app.models import Usuario
from app.schemas import UsuarioResponse

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("/", response_model=list[UsuarioResponse])
async def listar_usuarios(
    session: AsyncSession = Depends(get_session),
    current_user: Usuario = Depends(get_current_user),
):
    """Lista todos los usuarios (sin contraseñas)."""
    result = await session.execute(select(Usuario))
    usuarios = result.scalars().all()

    return [
        UsuarioResponse(
            id=u.id,
            username=u.username,
            email=u.email,
            nombres=u.nombres,
            apellidos=u.apellidos,
            estado=u.estado.value,
        )
        for u in usuarios
    ]

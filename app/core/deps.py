"""
Dependencias de seguridad y autenticación.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.core.database import get_session
from app.core.seguridad import verificar_token
from app.models import Usuario, EstadoCuenta

# Define el esquema de autenticación (apunta al endpoint de login)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_session)
) -> Usuario:
    """
    Valida el token JWT y recupera el usuario actual.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Validar token
    payload = verificar_token(token)
    if payload is None:
        raise credentials_exception

    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception

    # Buscar usuario en BD
    result = await session.execute(select(Usuario).where(Usuario.username == username))
    usuario = result.scalars().first()

    if usuario is None:
        raise credentials_exception

    # Validar estado del usuario
    if usuario.estado == EstadoCuenta.Baneado:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Usuario baneado"
        )

    if usuario.estado == EstadoCuenta.Suspendido:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Usuario suspendido"
        )

    if usuario.estado == EstadoCuenta.Eliminado:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Usuario eliminado"
        )

    return usuario

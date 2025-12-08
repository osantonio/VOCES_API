"""
Rutas de autenticación (registro y login).
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.core.database import get_session
from app.models import Usuario, EstadoCuenta
from app.schemas import UsuarioRegistro, UsuarioLogin, TokenResponse
from app.core.seguridad import hashear_password, verificar_password, crear_access_token

router = APIRouter(prefix="/auth", tags=["Autenticación"])


@router.post(
    "/registro", response_model=TokenResponse, status_code=status.HTTP_201_CREATED
)
async def registrar_usuario(
    datos: UsuarioRegistro, session: AsyncSession = Depends(get_session)
):
    """Registra un nuevo usuario."""
    # Verificar si el username ya existe
    result = await session.execute(
        select(Usuario).where(Usuario.username == datos.username)
    )
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El username ya está en uso"
        )

    # Verificar si el email ya existe
    result = await session.execute(select(Usuario).where(Usuario.email == datos.email))
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email ya está registrado",
        )

    # Crear usuario
    usuario = Usuario(
        username=datos.username,
        email=datos.email,
        password=hashear_password(datos.password),
        nombres=datos.nombres,
        apellidos=datos.apellidos,
        estado=EstadoCuenta.PendienteVerificacion,
    )

    session.add(usuario)
    await session.commit()
    await session.refresh(usuario)

    # Crear token
    access_token = crear_access_token(data={"sub": usuario.username})

    return TokenResponse(access_token=access_token)


@router.post("/login", response_model=TokenResponse)
async def login(datos: UsuarioLogin, session: AsyncSession = Depends(get_session)):
    """Inicia sesión y retorna un token JWT."""
    # Buscar usuario
    result = await session.execute(
        select(Usuario).where(Usuario.username == datos.username)
    )
    usuario = result.scalars().first()

    if not usuario or not verificar_password(datos.password, usuario.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if usuario.estado == EstadoCuenta.Baneado:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Usuario baneado"
        )

    if usuario.estado == EstadoCuenta.Suspendido:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Usuario suspendido"
        )

    # Crear token
    access_token = crear_access_token(data={"sub": usuario.username})

    return TokenResponse(access_token=access_token)

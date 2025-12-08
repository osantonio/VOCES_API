"""
Schemas de Pydantic para requests y responses.
"""

from pydantic import BaseModel


class UsuarioRegistro(BaseModel):
    """Schema para registro de usuario."""

    username: str
    email: str
    password: str
    nombres: str | None = None
    apellidos: str | None = None


class UsuarioLogin(BaseModel):
    """Schema para login de usuario."""

    username: str
    password: str


class TokenResponse(BaseModel):
    """Schema para respuesta de token JWT."""

    access_token: str
    token_type: str = "bearer"


class UsuarioResponse(BaseModel):
    """Schema para respuesta de datos de usuario."""

    id: int
    username: str
    email: str
    nombres: str | None
    apellidos: str | None
    estado: str

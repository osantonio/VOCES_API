"""
Modelos de datos.
"""

from typing import Optional
from sqlmodel import Field

from app.models.mixins import TimestampMixin
from app.models.enums import EstadoCuenta


class Usuario(TimestampMixin, table=True):
    """Modelo de Usuario."""

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True, max_length=50)
    email: str = Field(unique=True, index=True, max_length=255)
    password: str = Field(max_length=255)  # Hash de la contraseña

    # Información personal
    nombres: Optional[str] = Field(default=None, max_length=100)
    apellidos: Optional[str] = Field(default=None, max_length=100)

    # Estado de la cuenta
    estado: EstadoCuenta = Field(
        default=EstadoCuenta.PendienteVerificacion,
        description="Estado actual de la cuenta",
    )

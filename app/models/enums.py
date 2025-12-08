"""
Enumeraciones para los modelos.
"""

from enum import Enum


class EstadoCuenta(str, Enum):
    """Estado de la cuenta del usuario."""

    Activo = "Activo"  # Cuenta activa y verificada
    PendienteVerificacion = "PendienteVerificacion"  # Email no verificado
    Inactivo = "Inactivo"  # Cuenta desactivada por el usuario
    Suspendido = "Suspendido"  # Suspendido temporalmente
    Baneado = "Baneado"  # Baneado permanentemente

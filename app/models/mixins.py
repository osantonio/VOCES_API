"""
Mixins reutilizables para los modelos.
"""

from datetime import datetime
from sqlmodel import Field, SQLModel


class TimestampMixin(SQLModel):
    """Mixin para campos de auditoría de timestamps."""

    creado_en: datetime = Field(
        default_factory=datetime.now,
        nullable=False,
        description="Fecha de creación del registro",
    )
    actualizado_en: datetime = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
        nullable=False,
        description="Fecha de última actualización",
    )

# VOCES API - Implementación Básica

Implementación básica de FastAPI con SQLModel, PostgreSQL y autenticación JWT.

## Tecnologías

- **FastAPI**: Framework web moderno y rápido
- **SQLModel**: ORM basado en Pydantic y SQLAlchemy
- **PostgreSQL**: Base de datos relacional
- **asyncpg**: Driver asíncrono para PostgreSQL
- **bcrypt**: Hashing de contraseñas
- **JWT**: Autenticación con tokens

## Instalación

1. Crear entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus credenciales de PostgreSQL
```

4. Ejecutar la aplicación:
```bash
uvicorn main:app --reload
```

## Endpoints

- `GET /` - Información de la API
- `POST /registro` - Registrar nuevo usuario
- `POST /login` - Iniciar sesión
- `GET /usuarios` - Listar usuarios
- `GET /docs` - Documentación interactiva (Swagger)

## Estructura del Proyecto

```
VOCES API/
├── app/
│   ├── routes/           # Endpoints organizados por módulo
│   │   ├── main.py       # Ruta raíz
│   │   ├── auth.py       # Autenticación (registro/login)
│   │   └── usuarios.py   # Gestión de usuarios
│   ├── schemas/          # Schemas de Pydantic
│   │   └── usuario.py    # Schemas de usuario
│   ├── database.py       # Configuración de BD con SQLModel
│   ├── models.py         # Modelos de datos (Usuario)
│   ├── mixins.py         # Mixins reutilizables (TimestampMixin)
│   ├── enums.py          # Enumeraciones (EstadoCuenta)
│   └── auth.py           # Funciones de seguridad (bcrypt + JWT)
├── main.py               # Aplicación principal
├── requirements.txt      # Dependencias
├── .env.example          # Variables de entorno de ejemplo
└── README.md             # Este archivo
```

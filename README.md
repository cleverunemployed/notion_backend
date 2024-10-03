# notion_backend

notion_backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── mongodb_models.py
│   │   └── postgres_models.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── mongodb.py
│   │   └── postgres.py
│   ├── routers/
│       ├── __init__.py
│       ├── mongo_router.py
│       └── postgres_router.py
│
├── alembic/ # Для миграций с PostgreSQL
│
├── alembic.ini
├── requirements.txt
└── venv/

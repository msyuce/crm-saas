import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Alembic config objesi
config = context.config

# Logging ayarları
fileConfig(config.config_file_name)

# MODELLERİN METADATA'SINI BURADA TANIT
from app.db.base import Base
from app.models import tenant, user  # varsa diğer modelleri de ekleyebilirsin

target_metadata = Base.metadata

def run_migrations_offline():
    """Veritabanı bağlantısı olmadan migration üret."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Veritabanı bağlantısı ile migration üret."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


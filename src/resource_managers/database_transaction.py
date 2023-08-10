from contextlib import contextmanager
from functools import cache
from typing import Callable, ContextManager

from sqlalchemy import QueuePool
from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

DB_URI = "postgresql://admin:admin@localhost:5432/test_db"
POOL_SIZE = 10


def build_engine() -> Engine:
    return create_engine(
        DB_URI,
        poolclass=QueuePool,
        pool_size=POOL_SIZE,
    )


@cache
def db_pool_connexion_session() -> Callable[[], Session]:
    return sessionmaker(bind=build_engine(), autocommit=False, autoflush=True)


@contextmanager
def db_session() -> ContextManager[Session]:
    session: Session = db_pool_connexion_session()()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

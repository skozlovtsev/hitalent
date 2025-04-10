from sqlalchemy import create_engine, Engine, insert, select, delete, CursorResult
from os import environ
from ..model.meta import metadata_obj


_engine = create_engine(f"postgresql+psycopg2://{environ['PG_USER']}:{environ['PG_PASSWORD']}@{environ['PG_HOST']}/{environ['PG_DB']}")


class _Connection:
    def __init__(self, engine: Engine):
        self._engine = engine
        metadata_obj.create_all(self._engin)
    
    def exec(self, stmt: insert | select | delete):
        result: CursorResult = None
        with self._engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result
    

connection = _Connection(_engine)
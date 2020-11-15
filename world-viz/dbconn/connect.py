"""
Database connection utlities
"""
import logging
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.engine.result import RowProxy

class DBConnection():
    """
    Setup a database connection engine via SQLAlchemy
    """
    def __init__(self,
                 address="db",
                 port="5432",
                 user="world",
                 password="world123",
                 database="world-db") -> None:
        db = f"postgresql://{user}:{password}@{address}:{port}/{database}"
        self._engine = create_engine(db)
        self._logger = logging.getLogger(__name__)
        self._logger.info("Database connection initialized")

    @property
    def engine(self) -> Engine:
        """
        Returns a database engine that can be used to generate connections
        or be passed directly to some libraries e.g. pandas

        Returns:
            Engine: Database engine that can generate connections
        """
        return self._engine

    def query(self, sql_statement: str) -> List[RowProxy]:
        """
        Generate a connection object that can execute() sql statements
        When used in a with-statement,
        successful operations are committed and error cases are rolled back.

        Returns:
            Connection: SQLAlchemy Connection object with established Transaction.
        """
        with self._engine.begin() as conn:
            data = conn.execute(sql_statement)
        return data.fetchall()
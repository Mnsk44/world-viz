"""
Database connection utlities
"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

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

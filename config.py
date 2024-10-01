from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# define the Base class for declarative models
Base = declarative_base()

class DatabaseConfig:
    """
    Database configuration class to manage connection settings.
    """
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        """
        Returns a new session object.

        :return: A new SQLAlchemy session.
        """
        return self.Session()

    def close(self):
        """
        Closes the database connection.
        """
        self.engine.dispose()

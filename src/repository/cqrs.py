"""coding=utf-8."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:secure_pass_here@localhost:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()




from sqlalchemy.orm import scoped_session
from abc import ABC, abstractmethod

from domain.repository import ProductRepositoryAbstract
from repository import models


class UnitOfWorkAbstract(ABC):
    """
    Unit of work to allocate multiples repositories
    """
    shoppers: ProductRepositoryAbstract

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        """"
        Persist changes in the repositoryd
        """
        pass

    @abstractmethod
    def rollback(self):
        """
        Avoid write in the repositoryd if something fail
        """
        pass


class CQRSAbstract(ABC):
    storage: UnitOfWorkAbstract
    unified: UnitOfWorkAbstract


class UnitOfWorkPostgres(UnitOfWorkAbstract):
    """
    Unit of work to orchestrate the repositories which write and read from Postgres DB
    """

    def __init__(self, session_factory=SessionLocal):
        self.session_factory = scoped_session(session_factory)
        self.session = None

    def __enter__(self):
        self.session = self.session_factory
        self.products = models.Repository(session=self.session)

    def __exit__(self, *args):
        super().__exit__()
        self.session.remove()

    def commit(self):
        """
        To persist the changes in the Postgres DataBase
        """
        self.session.commit()

    def rollback(self):
        """
        Avoid write in Postgres if something fail
        """
        self.session.rollback()


class UnitOfWorkUnified(UnitOfWorkAbstract):
    def __init__(self, sqlalchemy_session_factory=SessionLocal):

        self.sqlalchemy_session_factory = scoped_session(sqlalchemy_session_factory)

    def __enter__(self):
        self.sqlalchemy_session = self.sqlalchemy_session_factory()
        self.products = models.RepositoryU(session=self.sqlalchemy_session)

    # def __exit__(self, *args):
    #     super().__exit__()
    #     self.sqlalchemy_session.remove()

    def commit(self):
        """
        To persist the changes in the Postgres DataBase
        """
        self.sqlalchemy_session.commit()

    def rollback(self):
        """
        Avoid write in Postgres if something fail
        """
        self.sqlalchemy_session.rollback()


class CQRS(CQRSAbstract):

    def __init__(self):
        self.storage = UnitOfWorkPostgres()
        self.unified = UnitOfWorkUnified()

    def synchronization(self):
        pass


cqrs = CQRS()

#!/usr/bin/env python3
"""
Database DB Class
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """adds user objet to database"""
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """returns the first row in the users table"""
        try:
            # Query the User table and find the first row w/ specified
            # input args
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            return None
        except InvalidRequestError:
            raise InvalidRequestError()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """uses find_user_by to locate user before updating"""
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            # check if the user item found in the table has a key
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError("does not correspond to a user attribute")

#!/usr/bin/python3
"""Module that contains DBStorage class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage():
    """Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                f'mysql+mysqldb://{user}:{password}@{host}/{database}',
                pool_pre_ping = True
                )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """Queries on the current database session"""
        objects = {}
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                results = self.__session.query(cls).all()
                for obj in results:
                    key = f"{cls.__name__}.{obj.id}"
                    objects[key] = obj
        else:
            if not issubclass(cls, BaseModel):
                raise TypeError(f"{cls} is not a subclass of BaseModel")
            results = self.__session.query(cls).all()
            for obj in results:
                key = f"{cls.__name__}.{obj.id}"
                objects[key] = obj
        return objects

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj = None):
        """Deletes from the current database session obj if not None"""
        if obj is not None:
            if obj in self.__session:
                self.__session.delete(obj)
                self.save()

    def reload(self):
        """Creates all tables in the database"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

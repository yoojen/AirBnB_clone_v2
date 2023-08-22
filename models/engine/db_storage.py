#!/usr/bin/python3
"""this module is db storage of thes system"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage:
    """define database storage of the sysytem"""
    __engine = None
    __session = None

    def __init__(self):
        """initiate db storage instances"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB))
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        print(cls.__class__.__name__)
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[cls]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
    
    def new(self, obj):
        """add new item  in the database"""
        self.__session.add(obj)

    def save(self):
        """commit item in the databse"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """deleteitem frm the database"""
        if obj is not None:
            self.__session.delete()

    def reload(self):
        """creates tables of all classes in the database"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session


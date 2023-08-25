#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if models.storage_envirn == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""

        @property
        def cities(self):
            """returns all instances of city """
            cities_obj = models.storage.all(City)
            list_of_city = []
            for city in cities_obj.values():
                if city.state_id == self.id:
                    list_of_city.append(city)
            return list_of_city

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

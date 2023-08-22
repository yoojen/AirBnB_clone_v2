#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128))
    cities = relationship('City', backref='state')
    """ State class """
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

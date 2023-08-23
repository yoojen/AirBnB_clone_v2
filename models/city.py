#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.storage_envirn == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        place = relationship("Place", backref="city")
    else:
        state_id = ""
        name = ""
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

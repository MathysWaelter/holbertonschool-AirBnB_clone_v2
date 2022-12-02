#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if (getenv("HBNB_TYPE_STORAGE") == 'db'):
        cities = relationship("City", cascade="all,delete", backref="state")
    else:
        @property
        def cities(self):
            """  getter attribute cities that returns the list of
            City instances with state_id equals to the current State.id """
            from models import storage
            allcities = storage.all(City)
            c = {}
            for k, v in allcities.items():
                if v.state_id == self.id:
                    c[k] = v
            return c

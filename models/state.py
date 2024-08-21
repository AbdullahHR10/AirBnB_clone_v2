#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade='all, delete-orphan')

    @property
    def cities_list(self):
        """Returns the list of City instances with state_id equals to
        the current State.id"""
        from models import storage
        all_cities = storage.all(City)
        city_list = []
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

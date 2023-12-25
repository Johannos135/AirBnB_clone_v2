#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from sqlachemy import (Column, String, ForeignKey)
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))

    state = relationship("State", cascade="all, delete, delete-orphan",
                         uselist=False)

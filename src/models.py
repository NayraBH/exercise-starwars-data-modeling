import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    name = Column(String(250), nullable=False)
    password = Column(String(40), nullable=False)
    email = Column(String(150), nullable=False)
    active = Column(Boolean)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    photo = Column(String(300))
    like = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    photo = Column(String(300))
    like = Column(Integer)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship(User)
    characters = relationship(Characters)
    planets = relationship(Planets)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
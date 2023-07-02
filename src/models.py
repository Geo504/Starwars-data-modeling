import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, DATETIME, Numeric
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'peoples'
    
    uid = Column(Integer, Sequence('uid_seq'), primary_key=True)
    name = Column(String(250), nullable=False)

class PeopleProperty(Base):
    __tablename__ = 'People_Properties'

    id = Column(String(250), primary_key=True)
    people_uid = Column(Integer, ForeignKey('peoples.uid'), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    created=Column(DATETIME, nullable=False)
    edited= Column(DATETIME, nullable=False)
    homeworld=Column(String(250), nullable=False)

    people_properties = relationship(People, backref='PeopleProperty', lazy=True)



class Planet(Base):
    __tablename__ = 'planets'

    uid = Column(Integer, Sequence('uid_seq'), primary_key=True)
    name = Column(String(250), nullable=False)


class PlanetProperty(Base):
    __tablename__ = 'Planet_Properties'

    id = Column(String(250), primary_key=True)
    vehicles_uid = Column(String(250), ForeignKey('planets.uid'))

    diameter= Column(Integer, nullable=False)
    rotation_period=Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    Population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    created=Column(DATETIME, nullable=False)
    edited= Column(DATETIME, nullable=False)

    people_properties = relationship(Planet, backref='PlanetProperty', lazy=True)


class Vehicle(Base):
    __tablename__ = 'vehicles'

    uid = Column(Integer, Sequence('uid_seq'), primary_key=True)
    name = Column(String(250), nullable=False)

class VehicleProperty(Base):
    __tablename__ = 'Vehicle_Properties'

    id = Column(String(250), primary_key=True)
    vehicle_uid = Column(Integer, ForeignKey('vehicles.uid'), nullable=False)

    model= Column(String(250), nullable=False)
    vehicle_class=Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    lenght = Column(Numeric(precision=10, scale=2), nullable=False)
    crew = Column(Integer, nullable=False)
    passengers=Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Numeric(precision=7, scale=2), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    created=Column(DATETIME, nullable=False)
    edited= Column(DATETIME, nullable=False)

    vehicle_properties = relationship(Vehicle, backref='VehicleProperty', lazy=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

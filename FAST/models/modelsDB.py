#se importan las librerias necesarias
from DB.conexion import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'tbUsers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)
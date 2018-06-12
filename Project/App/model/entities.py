from sqlalchemy import Column, Integer, String
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'users'
    #id = Column(Integer, primary_key=True)
    name = Column(String(50),primary_key=True)
    email = Column(String(50))
    password = Column(String(12))
class Image(connector.Manager.Base):
    __tablename__= 'images'
    path = Column(String(50),primary_key=True)





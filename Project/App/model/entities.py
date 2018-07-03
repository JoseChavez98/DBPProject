from sqlalchemy import Column, Integer, String, Sequence, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, backref

from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'users'
    name = Column(String(50),primary_key=True)
    email = Column(String(50))
    password = Column(String(12))


class Image(connector.Manager.Base):
    __tablename__= 'images'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    path = Column(String(50))
    likes = Column(Integer)
    user=Column(String(50))





from sqlalchemy import Column, Integer, String, Date, Float, Table
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=False)
    description = Column(String(500), unique=False)
    primary_support = Column(String(50), unique=False)

    def __init__(self,id=None, name=None, primary_support=None, description=None):
        self.id = id
        self.name = name
        self.primary_support = primary_support
        self.description = description

    def __repr__(self):
        return '<%s %s %s %s>' % (self.id, self.name, self.primary_support, self.description)

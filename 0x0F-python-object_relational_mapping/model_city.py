#!/usr/bin/python3
"""model state
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    __table_args__ = {'mysql_charset': 'latin1'}

    id = Column(INTEGER(11), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name

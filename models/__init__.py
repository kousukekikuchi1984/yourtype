# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import config

Base = declarative_base()

def create_db():
    engine = create_engine(config.sqlalchemy_url, **config.configs)
    Session = sessionmaker(bind=engine)
    db = Session()
    return db


class Operation(object):

    def __init__(self, db=None):
        if db is None:
            db = create_db()
        self.db = db


class UseCase(object):

    def __init__(self, db=None):
        if db is None:
            db = create_db()
        self.db = db


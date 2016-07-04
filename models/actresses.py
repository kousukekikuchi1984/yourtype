# -*- coding: utf-8 -*-

import sys, re, os

import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from models import Base, Operation, UseCase


class Actress(Base):
    __tablename__     = 'actresses'
    #
    id                = Column(Integer, primary_key=True)
    name              = Column(String, nullable=False)
    path              = Column(String, nullable=False)
    liked             = Column(Boolean)
    ## big five
    neuroticism       = Column(Integer)
    extraversion      = Column(Integer)
    openness          = Column(Integer)
    agreeableness     = Column(Integer)
    conscientiousness = Column(Integer)
    #
    created_at        = Column(DateTime, server_default='current_timestamp')
    deleted_at        = Column(DateTime)

    @classmethod
    def new(cls, **kwargs):
        assert False, "*** use bulk-insert instead of insersion one by one"


class ActressOp(Operation):

    numbers = range(1, 8)
    actresses = []

    def _pick_actress(self, tab):
        image_path = tab.img['src'] if tab.img else None
        name = tab.a['title'] if tab.a else None
        if image_path is None or name is None:
            return None
        return {
            "name": name,
            "image_path": image_path,
        }

    def parse(self, content):
        tree = BeautifulSoup(content, 'html.parser')
        tabs = tree.find_all(attrs={"class": "thumbnailBox"})
        actresses = [ self._pick_actress(t) for t in tabs if t is not None ]
        self.actresses.extend(actresses)

    def bulk_insert(self):
        self.db.bulk_insert_mappings(Actress, self.actresses)
        self.db.flush()
        return True

    def run(self):
        for n in self.numbers:
            content = GensunOp(self.db).run(n)
            self.parse(content)
        self.bulk_insert()


class GensunOp(Operation):

    path = 'http://gensun.org/list_ja_female_%s.html'

    def run(self, number):
        html = self.path % number
        result = requests.get(html)
        print(result.__dict__)
        assert result.status_code == 200
        return result.content



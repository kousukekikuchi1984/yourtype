# -*- coding: utf-8 -*-

import sys, re, os
import time

import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from config import config

from models import Base, Operation, UseCase


class Actress(Base):
    __tablename__     = 'actresses'
    #
    id                = Column(Integer, primary_key=True)
    name              = Column(String, nullable=False)
    image_path        = Column(String, nullable=False)
    local_path        = Column(String, nullable=False)
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
        #
        local_path = 'gensun.org/wid/%s' % image_path.split('/')[-1]
        return {
            "name": name,
            "image_path": image_path,
            "local_path": local_path,
        }

    def parse(self, content):
        tree = BeautifulSoup(content, 'html.parser')
        tabs = tree.find_all(attrs={"class": "thumbnailBox"})
        actresses = [ self._pick_actress(t) for t in tabs ]
        actresses = [ a for a in actresses if a is not None ]
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

    ### get one
    def get_one(self):
        actress = (self.db.query(Actress)
                .filter_by(liked=None)
                .filter_by(deleted_at=None)
                .order_by(Actress.id)
                ).first()
        local_path = self.get_image(actress.image_path)
        #
        actress.local_path = config.domain + local_path
        self.db.add(actress); self.db.flush()
        return {
            "id": actress.id,
            "name": actress.name,
            "image_path": actress.image_path,
            "local_path": actress.local_path,
        }

    def get_image(self, image_path):
        import urllib.request
        path = "images/%s" % image_path.split('/')[-1]
        if not os.path.exists(path):
            urllib.request.urlretrieve(image_path, path)
        path = "/%s" % path
        return path

    ###
    def tag_like(self, id, liked):
        actress = self.db.query(Actress).get(id)
        actress.liked = liked
        self.db.add(actress)
        self.db.flush()
        return True


class GensunOp(Operation):
    """ deprecated but not modified
    """

    path = 'gensun.org/list_ja_female_%s.html'

    def run(self, number):
        if number == 1:
            html = 'gensun.org/list_ja_female.html'
        else:
            html = self.path % number
        with open(html, "r") as f:
            content = f.read()
        return content


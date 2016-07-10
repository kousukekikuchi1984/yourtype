# -*- coding: utf-8 -*-

import ujson
from flask import Flask, json, request
import tenjin
from tenjin.helpers import *

from models import create_db
from models.actresses import ActressOp

engine = tenjin.Engine()

app = Flask(__name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.route("/")
def hello():
    return "kou2k"

@app.route("/actress")
def get_one():
    db = create_db()
    actress = ActressOp(db).get_one()
    if actress is None:
        return "completed"
    return engine.render('app/actress.html', actress)

@app.route("/actress/<id>", methods=["POST"])
def liked(id):
    jdict = request.json
    db = create_db()
    db.begin()
    ret = ActressOp(db).tag_like(id, jdict['liked'])
    assert ret
    db.commit()
    return ujson.dumps({"test": True})



if __name__ == "__main__":
    app.run()

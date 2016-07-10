# -*- coding: utf-8 -*-

import ujson
from flask import Flask, json, request
import tenjin
from tenjin.helpers import *

from models import create_db
from models.actresses import ActressOp

engine = tenjin.Engine()

app = Flask(__name__, static_url_path='/images', static_folder='images')


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

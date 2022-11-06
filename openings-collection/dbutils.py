from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask import current_app as app

load_dotenv()


def db():
    app.config[
        "MONGO_URI"
    ] = f'mongodb://{os.environ["MONGODB_USERNAME"]}:{os.environ["MONGODB_PASSWORD"]}@{os.environ["MONGODB_HOSTNAME"]}:27017/{os.environ["MONGODB_DATABASE"]}'
    mongo = PyMongo(app)
    return mongo.db


def select_opening(openings):
    _openings = db().openings.find()

    item = {}
    data = []

    for opening in _openings:
        item = {
            "name": opening["name"],
            "eco": opening["eco"],
            "moves": opening["moves"],
        }
        if openings == "all":
            data.append(item)
    return data


def add_opening(name, eco, moves):
    item = {"name": name, "eco": eco, "moves": moves}
    db().openings.insert_one(item)

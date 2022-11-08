from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo, ObjectId
from flask import current_app as app

load_dotenv()


def db():
    app.config[
        "MONGO_URI"
    ] = f'mongodb://{os.environ["MONGODB_USERNAME"]}:{os.environ["MONGODB_PASSWORD"]}@{os.environ["MONGODB_HOSTNAME"]}:27017/{os.environ["MONGODB_DATABASE"]}'
    mongo = PyMongo(app)
    return mongo.db

def select_opening(key, value):
    return list(db().openings.find({key: value}))

def select_all_opening():
    return list(db().openings.find())

def add_opening(name, eco, moves):
    _openings_names = db().openings.distinct("name")
    item = {"name": name, "eco_code": eco, "moves": moves}
    if item["name"] not in _openings_names and item["name"]:
        db().openings.insert_one(item)

def delete_opening(op_name):
    db().openings.delete_one({"name": op_name})

def edit_opening(name, new_name, eco_code, moves):
    new_record = {"$set": {"name": new_name, "eco_code": eco_code, "moves": moves}}
    db().openings.find_one_and_update({"name": name}, new_record)

def add_game(white, black, opening, moves, result):
    game = {"white": white, "black": black, "opening": opening, "moves": moves, "result": result}
    if moves:
        db().games.insert_one(game)

def select_all_games():
    return list(db().games.find())

def delete_game(_id):
    db().games.delete_one({"_id": ObjectId(_id)})
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo, ObjectId
from flask import current_app as app

load_dotenv()
def db():
    app.config[
        "MONGO_URI"
    ] = f'mongodb://{os.environ["MONGODB_USERNAME"]}:{os.environ["MONGODB_PASSWORD"]}@{os.environ["MONGODB_HOSTNAME"]}:27017/{os.environ["MONGODB_DATABASE"]}?authSource=admin'
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
    game = {
        "white": white,
        "black": black,
        "opening": opening,
        "moves": moves,
        "result": result,
    }
    if moves:
        db().games.insert_one(game)


def select_all_games():
    return list(db().games.find())


def select_game(_id):
    return list(db().games.find({"_id": ObjectId(_id)}))


def delete_game(_id):
    db().games.delete_one({"_id": ObjectId(_id)})


def edit_game(_id, white, black, moves, result):
    new_record = {
        "$set": {"white": white, "black": black, "moves": moves, "result": result}
    }
    db().games.find_one_and_update({"_id": ObjectId(_id)}, new_record)


def searched_games(query):
    # Could be simplicitied (if white==black==opening -> 3 records will appear)
    output = []
    for key in ["white", "black", "opening"]:
        result = list(db().games.find({key: query}))
        if result:
            output.append(result)
    return [item for sublist in output for item in sublist]


def searched_opening(query):
    for key in ["name", "eco_code"]:
        data = select_opening(key, query)
        if data:
            return data

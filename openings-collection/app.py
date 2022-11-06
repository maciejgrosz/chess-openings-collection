from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo
import dbutils

load_dotenv()
app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    if request.method == "GET":
        try:
            dbutils.health_db()
            output = "Database is ok"
            status = 200
        except Exception as e:
            output = str(e)
            status = 500
        return output, status


@app.route("/")
def index():
    return jsonify(status=True, message="Welcome to the Dockerized Flask MongoDB app!")


@app.route("/openings")
def openings():
    data = dbutils.select_opening("all")
    return jsonify(status=True, data=data)


@app.route("/add_opening", methods=["POST", "GET"])
def create_opening():
    # data = request.get_json(force=True)
    dbutils.add_opening()
    return jsonify(status=True, message="Opening saved successfully!"), 201

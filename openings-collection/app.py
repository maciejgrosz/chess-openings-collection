from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo
import dbutils

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/openings")
def openings():
    data = dbutils.select_opening("all")
    return jsonify(status=True, data=data)


@app.route("/add_opening", methods=["POST", "GET"])
def create_opening():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        name = request.form.get("name")
        eco = request.form.get("eco_code")
        moves = request.form.get("moves")
    dbutils.add_opening(name, eco, moves)
    return jsonify(status=True, message="Opening saved successfully!"), 201

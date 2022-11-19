from flask import Blueprint, Flask, request, jsonify, render_template, redirect, url_for, Response
from dotenv import load_dotenv
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time
from flask_pymongo import PyMongo
import dbutils

bp = Blueprint('bp', __name__, url_prefix='/')

_INF = float("inf")
graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The totoal number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', "Histogram for the druation in seconds.", buckets =(1,2,5,6,10,_INF))

@bp.route("/", methods=["POST", "GET"])
def show_openings():
    start_time = time.time()
    graphs['c'].inc()
    if request.method == "GET":
        data = dbutils.select_all_opening()
        end_time = time.time()
        graphs['h'].observe(end_time-start_time)
        return render_template("index.html", title="Openings", openings=data)
    if request.method == "POST":
        search_query = request.form.get("search")
        data = dbutils.searched_opening(search_query)
        end_time = time.time()
        graphs['h'].observe(end_time-start_time)
        return render_template("index.html", title="Openings", openings=data)


@bp.route("/add_opening", methods=["POST", "GET"])
def create_opening():
    if request.method == "GET":
        return render_template("add_opening.html")
    if request.method == "POST":
        name = request.form.get("name")
        eco_code = request.form.get("eco_code")
        moves = request.form.get("moves")
    dbutils.add_opening(name, eco_code, moves)
    return redirect(url_for("show_openings"))


@bp.route("/delete/<name>")
def delete_opening(name):
    dbutils.delete_opening(name)
    return redirect(url_for("show_openings"))


@bp.route("/edit/<name>", methods=["GET", "POST"])
def edit_opening(name):
    if request.method == "GET":
        data = dbutils.select_opening("name", name)[0]
        return render_template(
            "edit_opening.html",
            op_name=data["name"],
            eco_code=data["eco_code"],
            moves=data["moves"],
        )
    if request.method == "POST":
        new_name = request.form.get("name")
        eco_code = request.form.get("eco_code")
        moves = request.form.get("moves")
        dbutils.edit_opening(name, new_name, eco_code, moves)
        return redirect(url_for("show_openings"))


@bp.route("/add_game/<opening_name>", methods=["GET", "POST"])
def add_game(opening_name):
    if request.method == "POST":
        player_white = request.form.get("player_white")
        player_black = request.form.get("player_black")
        moves = request.form.get("moves")
        result = request.form.get("result")
        dbutils.add_game(player_white, player_black, opening_name, moves, result)
        return redirect(url_for("show_games"))
    if request.method == "GET":
        data = dbutils.select_opening("name", opening_name)[0]
        return render_template("add_game.html", title="Openings", opening=data["name"])


@bp.route("/show_games", methods=["POST", "GET"])
def show_games():
    if request.method == "GET":
        data = dbutils.select_all_games()
        return render_template("show_games.html", games=data)
    if request.method == "POST":
        query = request.form.get("search")
        data = dbutils.searched_games(query)
        return render_template("show_games.html", games=data)


@bp.route("/delete/game/<_id>")
def delete_game(_id):
    dbutils.delete_game(_id)
    return redirect(url_for("show_games"))


@bp.route("/edit/game/<_id>", methods=["GET", "POST"])
def edit_game(_id):
    if request.method == "POST":
        white = request.form.get("player_white")
        black = request.form.get("player_black")
        moves = request.form.get("moves")
        result = request.form.get("result")
        dbutils.edit_game(_id, white, black, moves, result)
        return redirect(url_for("show_games"))
    if request.method == "GET":
        game = dbutils.select_game(_id)[0]
        return render_template(
            "edit_game.html",
            id=_id,
            white=game["white"],
            black=game["black"],
            opening=game["opening"],
            moves=game["moves"],
            result=game["result"],
        )


@bp.route("/health", methods=["GET"])
def health_check():
    if request.method == "GET":
        return jsonify(status=200)

@bp.route("/metrics", methods=["GET"])
def metrics():
    res = []
    for _, v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app

app = create_app()


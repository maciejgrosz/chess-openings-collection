import os
import sys

sys.path.insert(1, os.getcwd())
import dbutils as dbutils
import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    ctx = app.app_context()
    ctx.push()
    with ctx:
        pass

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_add_opening(client):
    dbutils.add_opening("test_name", "test_eco", "test_moves")
    response = client.get("/")
    assert b"<td>test_name</td>" in response.data


def test_add_game(client):
    dbutils.add_game(
        "test_white", "test_black", "test_opening", "test_moves", "test_result"
    )
    response = client.get("/show_games")
    assert b"<td>test_moves</td>" in response.data


def test_edit_opening(client):
    dbutils.edit_opening("test_name", "new_test_name", "test_eco", "test_moves")
    response = client.get("/")
    assert b"<td>new_test_name</td>" in response.data


def test_delete_opening(client):
    dbutils.delete_opening("new_test_name")
    response = client.get("/")
    assert b"<td>new_test_name</td>" not in response.data

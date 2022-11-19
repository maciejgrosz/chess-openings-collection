import pytest
import sys
import os

sys.path.insert(1, os.getcwd())
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

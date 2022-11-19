import pytest
import os
import sys
sys.path.insert(1, os.getcwd())
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_health_check(client):
    response = client.get("/health")
    assert  b"200" in response.data

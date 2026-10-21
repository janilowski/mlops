import pytest
from fastapi.testclient import TestClient

from training import save_model, train_model


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    save_model(train_model())

    from app import app

    with TestClient(app) as client:
        yield client

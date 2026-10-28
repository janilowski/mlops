from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("I love this product!", "positive"),
        ("I hate this product!", "negative"),
        ("This is a chair.", "neutral"),
    ],
)
def test_predict(text: str, expected: str) -> None:
    with TestClient(app) as client:
        response = client.post("/predict", json={"text": text})

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"prediction": expected}


@pytest.mark.parametrize(
    "payload", [{}, {"text": ""}, {"text": " "}, {"text": 42}, {"text": None}]
)
def test_invalid_text(payload: dict[str, object]) -> None:
    with TestClient(app) as client:
        response = client.post("/predict", json=payload)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["loc"] == ["body", "text"]

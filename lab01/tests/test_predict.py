from http import HTTPStatus

import pytest


@pytest.mark.parametrize(
    ("features", "expected"),
    [
        ([5.1, 3.5, 1.4, 0.2], "setosa"),
        ([7.0, 3.2, 4.7, 1.4], "versicolor"),
        ([6.3, 3.3, 6.0, 2.5], "virginica"),
    ],
)
def test_predict(client, features, expected):
    # JSON field order must not affect the feature order used by the model.
    response = client.post(
        "/predict",
        json={
            "petal_width": features[3],
            "petal_length": features[2],
            "sepal_width": features[1],
            "sepal_length": features[0],
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"prediction": expected}


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {
            "sepal_length": "invalid",
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    ],
)
def test_predict_rejects_invalid_features(client, payload):
    response = client.post("/predict", json=payload)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

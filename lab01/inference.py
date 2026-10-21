from pathlib import Path

import joblib
from sklearn.tree import DecisionTreeClassifier


IRIS_CLASS_NAMES = ("setosa", "versicolor", "virginica")


def load_model(path: str | Path = "model.joblib") -> DecisionTreeClassifier:
    return joblib.load(path)


def predict(model: DecisionTreeClassifier, features: list[float]) -> str:
    prediction = model.predict([features])[0]
    return IRIS_CLASS_NAMES[prediction]

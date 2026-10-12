from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import Bunch


def load_data() -> Bunch:
    return load_iris()


def train_model() -> DecisionTreeClassifier:
    data = load_data()
    model = DecisionTreeClassifier(random_state=42)
    model.fit(data.data, data.target)
    return model


def save_model(
    model: DecisionTreeClassifier, path: str | Path = "model.joblib"
) -> None:
    joblib.dump(model, path)


if __name__ == "__main__":
    save_model(train_model())

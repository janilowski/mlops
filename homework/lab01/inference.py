from pathlib import Path

import joblib  # type: ignore[import-untyped]
from sentence_transformers import SentenceTransformer


_MODEL_DIR = Path(__file__).with_name("model")
_SENTIMENTS = ("negative", "neutral", "positive")

_encoder = SentenceTransformer(
    str(_MODEL_DIR / "sentence_transformer.model"), device="cpu", local_files_only=True
)
_classifier = joblib.load(_MODEL_DIR / "classifier.joblib")


def predict(text: str) -> str:
    return _SENTIMENTS[_classifier.predict(_encoder.encode([text]))[0]]

from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict as predict_iris


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = load_model()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    features = [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    ]
    prediction = predict_iris(app.state.model, features)
    return PredictResponse(prediction=prediction)

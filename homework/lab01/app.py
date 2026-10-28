from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

from inference import predict as predict_sentiment


class PredictRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    text: str = Field(min_length=1)


class PredictResponse(BaseModel):
    prediction: str


app = FastAPI()


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction=predict_sentiment(request.text))

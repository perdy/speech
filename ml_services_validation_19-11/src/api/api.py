import json

import typing
from urllib.parse import unquote

import uvicorn
from flama.components import Component
from keras.models import load_model
from keras.preprocessing import sequence
from marshmallow import Schema, fields

from flama.applications import Flama

MAX_WORDS = 500
VOCABULARY_LENGTH = 20000


class SentimentAnalysisModel:
    def __init__(self, model, words: typing.Dict[str, int]):
        self.model = model
        self.words = words

    def predict(self, text: str) -> typing.Tuple[float, str]:
        x = text.lower().split()
        x = [self.words.get(i, 0) if self.words.get(i, 0) <= VOCABULARY_LENGTH else 0 for i in x]
        x = sequence.pad_sequences([x], maxlen=MAX_WORDS)
        score = self.model.predict(x)
        sentiment = "Positive" if self.model.predict_classes(x)[0][0] == 1 else "Negative"

        return score, sentiment


class SentimentAnalysisModelComponent(Component):
    def __init__(self, model_path: str, words_path: str):
        self.model = load_model(model_path)
        self.model._make_predict_function()
        with open(words_path) as f:
            self.words = json.load(f)

    def resolve(self) -> SentimentAnalysisModel:
        return SentimentAnalysisModel(model=self.model, words=self.words)


class SentimentAnalysis(Schema):
    text = fields.String(title="text", description="Text to analyze")
    score = fields.Float(title="score", description="Sentiment score in range [0,1]")
    sentiment = fields.String(title="sentiment", description="Sentiment class (Positive or Negative)")


def analyze(text: str, model: SentimentAnalysisModel) -> SentimentAnalysis:
    """
    tags:
        - sentiment-analysis
    summary:
        Sentiment analysis.
    description:
        Performs a sentiment analysis on a given text.
    responses:
        200:
            description: Analysis result.
    """
    text = unquote(text)
    score, sentiment = model.predict(text)

    return {"text": text, "score": score, "sentiment": sentiment}


app = Flama(
    components=[SentimentAnalysisModelComponent(model_path="model.h5", words_path="words.json")],
    title="Sentiment Analysis",  # API title
    version="0.1",  # API version
    description="A sentiment analysis API for movies reviews",  # API description
    redoc="/redoc/",
)

app.add_route("/analyze/", analyze, methods=["GET"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

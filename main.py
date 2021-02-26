from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from model.keywords import createModels, getKey 

class Params(BaseModel):
    text: str
    ngram: Optional[tuple] = (1,2)
    diversity: Optional[float] = 0.2
    lang: Optional[str] = None

app = FastAPI()

models = createModels()

@app.post("/keywords")
def create_params(params: Params):
    texto = params.text
    ngram = params.ngram
    diversity = params.diversity
    lang = params.lang

    keys = getKey(texto, models, ngram, diversity, lang)

    return keys
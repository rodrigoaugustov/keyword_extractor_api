import sys

sys.path.append('.')

from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
from flair.embeddings import TransformerDocumentEmbeddings
from textblob import TextBlob

from utils.textprocess import preprocess_text


def createModels():
    sentence_pt = TransformerDocumentEmbeddings('neuralmind/bert-large-portuguese-cased')
    sentence_en = SentenceTransformer('xlm-r-bert-base-nli-stsb-mean-tokens')
    model_pt = KeyBERT(model=sentence_pt)
    model_en = KeyBERT(model=sentence_en)

    return model_pt, model_en


def getKey(text, models, ngram=(1, 2), diversity=0.2, lang=None):
    if lang != 'pt-br' and lang != 'en-us':
        lang = TextBlob(text).detect_language()

    if 'pt' in lang:
        model = models[0]
        keywords = model.extract_keywords(text, keyphrase_ngram_range=ngram, use_mmr=True, diversity=diversity)
        keywords = dict(keywords)
        all_keys = [i for i in dict(keywords).keys()]
        return all_keys

    elif 'en' in lang:
        model = models[1]
        keywords = model.extract_keywords(text, keyphrase_ngram_range=ngram, use_mmr=True, diversity=diversity)
        keywords = dict(keywords)
        all_keys = [i for i in dict(keywords).keys()]
        return all_keys

    else:
        raise Exception(
            'Desculpe, não conseguimos identificar o idioma. Por favor refaça a solicitação informando o idioma')

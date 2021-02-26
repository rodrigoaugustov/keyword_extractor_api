# Keywords Extractor - API
A simple keywords extractor built using FASTApi and KeyBert.

FASTApi - https://fastapi.tiangolo.com/
<br>KeyBert - https://github.com/MaartenGr/KeyBERT/

Model are built to work with English and Portuguese texts.
<br>English: 'xlm-r-bert-base-nli-stsb-mean-tokens' 
<br>Portuguese: 'neuralmind/bert-large-portuguese-cased'

Auto language detect it's working, but it's possible set the lang as a param on body request.

## Usage
- To start API locally just run:
```
uvicorn main:app --reload
```

First run may take a while to download the BERT Models.
The auto generated documentation is available on 'localhost:8000/docs' route

The POST requests must be send to 'localhost:8000/keywords' with the following params:
```
{
"text": "TEXT TO GET KEYWORDS FROM"
"ngram": [n,n] (Optional param, to define ngram range to extract. Default = [1,2]
"diversity": float between 0 ~ 1 (Optional param, to define if want get more precises (0) or more diversity keywords (1). Default = 0.2
"lang": string (Optional param, to force the lang recognize. Default = None (autodetect))
}
```
The response will be a list with the 5 keywords / keyphrases.

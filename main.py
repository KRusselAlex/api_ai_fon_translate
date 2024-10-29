from fastapi import FastAPI
# from flask import Flask
from deep_translator import GoogleTranslator




app = FastAPI()


@app.get("/")
def read_root():
    translated = GoogleTranslator(source='fr', target='fon').translate("Bonsoir. Comment vas-tu ?")
    text = translated
    

    return {"data": text, "status": 200}


@app.get("/create_text/{item}")
def createText(item: str):
    print(item)
    untranslated = item  
    translated = GoogleTranslator(source='fr', target='fon').translate(untranslated)
    text = translated

    return {"data": text, "status": 200}
from fastapi import FastAPI
# from flask import Flask
from deep_translator import GoogleTranslator
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    texts: str | None = None
    
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

@app.post("/create_fon/")
async def create_fon(text_data: Item):
    print(text_data.texts)
    untranslated = text_data.texts  
    translated = GoogleTranslator(source='fr', target='fon').translate(untranslated)
    text = translated

    return {"data": text, "status": 200}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
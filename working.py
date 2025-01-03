from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"Data": "Testing"}

@app.get('/about')
def home():
    return {"Data": "About"}
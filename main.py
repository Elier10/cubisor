import requests
from fastapi import FastAPI, APIRouter
from models import Code
from functions import CUBISOR

app = FastAPI()

@app.get("/cubisor/data")
def get_data():
    response = "HOLA"
    return response

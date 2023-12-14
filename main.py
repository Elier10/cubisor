import requests
from fastapi import FastAPI, APIRouter
from models import Code
from functions import CUBISOR

app = FastAPI()

@app.get("/cubisor/data")
def get_data():
    response = requests.get(r"http://localhost:8000/cubisor/data")
    return response

import os
import requests
from flask import Blueprint
from dotenv import load_dotenv

load_dotenv()

ETL_CAMARA_HOST = os.getenv('ETL_CAMARA_HOST')
ETL_CAMARA_PORT = os.getenv('ETL_CAMARA_PORT')

base_url = f"{ETL_CAMARA_HOST}:{ETL_CAMARA_PORT}"

camara = Blueprint('camara', __name__, url_prefix='/camara')

@camara.route('/')
def index():
    return "Camara"

@camara.route('/deputies')
def deputies():
    r = requests.get(f'http://{base_url}/api/deputies')
    return r.json()

@camara.route('profile/<id>')
def profile(id):
    r = requests.get(f'http://{base_url}/api/{id}')
    return r.json()

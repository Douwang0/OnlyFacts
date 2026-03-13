from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('KEY') #Nom anglais car librairie

from . import routes # On utilise . pour utiliser le app deja import
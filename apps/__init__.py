from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.getenv('KEY') #Nom anglais car librairie

from . import routes # On utilise . pour utiliser le app deja import
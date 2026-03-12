from flask import Flask

app = Flask(__name__)

from . import routes # On utilise . pour utiliser le app deja import
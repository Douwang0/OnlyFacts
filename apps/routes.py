from . import app # On utilise . pour utiliser le app deja import

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
from flask import render_template
from . import app # On utilise . pour utiliser le app deja import

@app.route('/')
@app.route('/index')
def index():
    utilisateur = {'nom': 'Giulian'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ] # Dico de test, pas d'anglais dans la prod
    return render_template('index.html', titre='Accueil', utilisateur=utilisateur, posts=posts)
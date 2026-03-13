from flask import render_template, request, session, g
from apps.db import db_test_user, db_test_posts
from . import app # On utilise . pour utiliser le app deja import

@app.before_request
def charger_utilisateur():
    """
    Permet d'acceder a l'utilisateur avec g.utilisateur sans faire la requete dans la fonction
    Execute a chaque requete
    """
    id = session.get("user_id")

    if id:
        g.utilisateur = db_test_user[id]
    else:
        g.utilisateur = None

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titre='Accueil', utilisateur=g.utilisateur, posts=db_test_posts)



#Page de test, a enlever
@app.route('/form', methods = ['POST','GET'])
def form():
    if request.method == 'POST':
        info = request.form['info']
        info_cachee = request.form['info_cachee']

        print(info,info_cachee)
    return render_template('form.html')
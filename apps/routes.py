from flask import render_template, request, session, g, redirect
from apps.db import db_test_user, db_test_posts
from apps.auth import get_utilisateur
from . import app # On utilise . pour utiliser le app deja import

@app.before_request
def charger_utilisateur():
    """
    Permet d'acceder a l'utilisateur avec g.utilisateur sans faire la requete dans la fonction
    Execute a chaque requete
    """
    id = session.get("user_id")
    if id is not None:
        g.utilisateur = db_test_user[id]
    else:
        g.utilisateur = None

@app.route('/')
@app.route('/index')
def index():
    if g.utilisateur is None:
        return redirect(location="/login")
    return render_template('index.html', titre='Accueil', utilisateur=g.utilisateur, posts=db_test_posts)

@app.route('/login', methods = ['POST','GET'])
def login():
    erreur = False
    if request.method == 'POST':
        id_utilisateur = get_utilisateur(request.form['nom'],request.form['prenom'],request.form['mdp'])
        if id_utilisateur == "Aucun":
            erreur = "Aucun"
        elif id_utilisateur is False:
            erreur = True
        else:
            session['user_id'] = id_utilisateur
            return redirect('/')
    return render_template('login.html', erreur=erreur)

#Page de test, a enlever
@app.route('/form', methods = ['POST','GET'])
def form():
    if request.method == 'POST':
        info = request.form['info']
        info_cachee = request.form['info_cachee']

    return render_template('form.html')
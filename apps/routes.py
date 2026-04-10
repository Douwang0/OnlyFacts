from flask import render_template, request, session, g, redirect
from apps.db import get_utilisateur_par_id, creer_post, get_tous_posts
from apps.auth import get_utilisateur, set_utilisateur
from apps.post import liste_post_fini
from . import app # On utilise . pour utiliser le app deja import

DEFAULT_PARAMETRES = ("",20,False,"created")

@app.before_request
def charger_utilisateur():
    """
    Permet d'acceder a l'utilisateur avec g.utilisateur sans faire la requete dans la fonction
    Execute a chaque requete
    """
    id = session.get("user_id")
    if id is not None:
        g.utilisateur = get_utilisateur_par_id(id)
    else:
        g.utilisateur = None

@app.route('/')
@app.route('/index')
def index():
    if g.utilisateur is None:
        return redirect(location="/login")    
    return render_template('index.html', titre='Accueil', utilisateur=g.utilisateur, posts=liste_post_fini())

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

@app.route('/register', methods = ['POST','GET'])
def register():
    erreur = False
    if request.method == 'POST':
        if request.form['mdp'] == request.form['mdp_verif']:
            erreur = set_utilisateur(request.form['nom'],request.form['prenom'],request.form['mdp'])
        else:
            erreur = "Difference Mdp"
        if erreur is False:
            return redirect('/login')
    return render_template('signin.html', erreur=erreur)

@app.route('/search', methods = ['GET'])
def search():
    if g.utilisateur is None:
        return redirect(location="/login")
    if not session.get("parametres"):
        session["parametres"] = DEFAULT_PARAMETRES
    parametres = session.get("parametres")

    return render_template('search.html', titre='Recherche', utilisateur=g.utilisateur, posts=liste_post_fini(*parametres), parametres=parametres)


@app.route('/create_post', methods = ['POST'])
def create_post():
    if request.method == 'POST':
        contenu = request.form['contenu']
        creer_post(g.utilisateur["id"], contenu)
    return redirect("/")

@app.route('/filtrer', methods = ['POST'])
def filtrer():
    texte = request.form["texte"]
    max = request.form['max']
    if not isinstance(max,str) or not max.isnumeric() or int(max) < 0:
        max = DEFAULT_PARAMETRES[1]
    else:
        max = int(max)

    long = len(get_tous_posts())
    if max > long:
        max = long
    ordre = request.form['ordre'] # Croissant True/False
    if ordre == "croissant" : ordre = True
    else: ordre = False
    cle = request.form['cle']

    session["parametres"] = (texte,max,ordre,cle)
    return redirect("/search")

@app.route('/reset_filtre', methods = ['POST'])
def reset():
    session["parametres"] = ("",20,False,"created")
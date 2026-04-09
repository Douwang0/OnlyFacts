from flask import render_template, request, session, g, redirect
from apps.data import get_utilisateur_par_id, creer_post, get_tous_posts
from apps.auth import get_utilisateur, set_utilisateur
from apps.post import liste_post_fini
from . import app # On utilise . pour utiliser le app deja import

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
    parametres = session.get("parametres")
    if not parametres:
        parametres = (0,20,False,"created")
    
    return render_template('index.html', titre='Accueil', utilisateur=g.utilisateur, posts=liste_post_fini(*parametres))

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
    parametres = session.get("parametres")
    if not parametres:
        session["parametres"] = ("",20,False,"created")
    
    return render_template('search.html', titre='Recherche', utilisateur=g.utilisateur, posts=liste_post_fini(*parametres))


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
    if max < 0 or not max.isnumeric():
        max = 0
    else:
        max = int(min)
    max = request.form['max']

    long = len(get_tous_posts())
    if max > long:
        max = long
    ordre = request.form['ordre'] # Croissant True/False
    if ordre == "croissant" : ordre = True
    else: ordre = False
    cle = request.form['cle']

    session["parametres"] = (texte,min,max,ordre,cle)

@app.route('/reset_filtre', methods = ['POST'])
def reset():
    session["parametres"] = ("",20,False,"created")

#Page de test, a enlever
@app.route('/form', methods = ['POST','GET'])
def form():
    if request.method == 'POST':
        info = request.form['info']
        info_cachee = request.form['info_cachee']

    return render_template('form.html')
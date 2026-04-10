from time import time
from apps.db import db_test_user, db_test_posts, db_test_votes

# recherche_db_temp,ajouter_db_temp

#def recherche_utilisateur(nom,prenom): #Besoin d'un vraie func de db
#    """Si db a combinason nom prenom, renvoyer id,nom,prenom,mdp(hash) sinon None"""
#    for utilisateur in db_test_user:
#        if utilisateur["nom"] == nom and utilisateur["prenom"] == prenom:
#            return utilisateur
       
def ajouter_utilisateur(nom,prenom,mdp_hash):
 # déterminer le nouvel id
    if len(db_test_user) == 0:
        nouvel_id = 1
    else:
        nouvel_id = db_test_user[-1]["id"] + 1
    nouveau_user = {
        "id": nouvel_id, 
        "nom": nom, 
        "prenom": prenom, 
        "mdp": mdp_hash
        }
    db_test_user.append(nouveau_user)
    return nouveau_user
    
def creer_post(id_utilisateur, contenu):

    # déterminer le nouvel id
    if len(db_test_posts) == 0:
        nouvel_id = 1
    else:
        nouvel_id = db_test_posts[-1]["id"] + 1

    nouveau_post = {
        "id": nouvel_id,
        "author_id": id_utilisateur,
        "body": contenu,
        "created": time()
    }

    db_test_posts.append(nouveau_post)

    return nouveau_post

def get_utilisateur_par_id(id_utilisateur):
    for utilisateur in db_test_user:
        if utilisateur["id"] == id_utilisateur:
            return utilisateur
    return None


def get_tous_posts():
    return db_test_posts


def get_votes_post(id_post):
    return sum(1 for vote in db_test_votes if vote["post_id"] == id_post)


def utilisateur_a_vote(id_utilisateur, id_post):
    for vote in db_test_votes:
        if vote["user_id"] == id_utilisateur and vote["post_id"] == id_post:
            return True
    return False


def get_posts_avec_infos(texte):
    posts_prepares = []
    post_avec_mots = rechercher_post(texte)
    
    for post in db_test_posts:

        auteur = get_utilisateur_par_id(post["author_id"])
        votes = get_votes_post(post["id"])

        posts_prepares.append({
            "id": post["id"],
            "body": post["body"],
            "created": post["created"],
            "auteur": auteur,
            "votes": votes
        })

    return posts_prepares

def rechercher_post(texte):
    # INCLURE SEARCH AVEC LE SQL
    pass
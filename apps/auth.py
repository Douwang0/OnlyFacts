from apps.mdp import crypter, check
from apps.db import db_test_user

def recherche_db_temp(nom,prenom):
    """Si db a combinason nom prenom, renvoyer id,nom,prenom,mdp(hash) sinon None"""
    for id in range(len(db_test_user)):
        if db_test_user[id]["nom"] == nom and db_test_user[id]["prenom"] == prenom:
            temp = db_test_user[id].copy()
            temp["id"] = id
            return temp

def get_utilisateur(nom,prenom,mdp): # A refaire quand j'aurais les func de db pour les vraies info
    utilisateur = recherche_db_temp(nom,prenom)
    if utilisateur:
        if check(mdp,utilisateur["mdp"]):
            return utilisateur["id"]
        else:
            return False
    else:
        return "Aucun"
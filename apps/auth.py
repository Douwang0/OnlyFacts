from apps.mdp import crypter, check
from apps.db import db_test_user

def recherche_db_temp(nom,prenom): #Besoin d'un vraie func de db
    """Si db a combinason nom prenom, renvoyer id,nom,prenom,mdp(hash) sinon None"""
    for id in range(len(db_test_user)):
        if db_test_user[id]["nom"] == nom and db_test_user[id]["prenom"] == prenom:
            temp = db_test_user[id].copy()
            temp["id"] = id
            return temp
def ajouter_db_temp(nom,prenom,mdp_hash):
    db_test_user.append(
        {
            "nom" : nom,
            "prenom" : prenom,
            "mdp" : mdp_hash
        }
    )

def get_utilisateur(nom,prenom,mdp): 
    """ Donne l'id utilisateur si les infos sont correctes, si combi n'exisite pas 'Aucun,et si mdp Incorect False'"""
    utilisateur = recherche_db_temp(nom,prenom)
    if utilisateur:
        if check(mdp,utilisateur["mdp"]):
            return utilisateur["id"]
        else:
            return False
    else:
        return "Aucun"
    
def set_utilisateur(nom,prenom,mdp):
    """Essaie de cree un utilisateur et revoie une erreur si besoin sinon False"""
    if recherche_db_temp(nom,prenom):
        return "Existant"
    elif nom == "" or prenom == "":
        return "Nom/Prenom Vide"
    elif len(mdp) < 7: # 8+ pour un mot de passe robuste
        return "Mdp trop court"
    else:
        ajouter_db_temp(nom,prenom,crypter(mdp))
        return False
from apps.mdp import crypter, check
from apps.db import get_utilisateur_par_info, ajouter_utilisateur

def recherche_utilisateur(nom,prenom):
    """Prend une liste d'utilisateur par nom prenom et renvoie soit un seul utilisateur soit None si aucun trouvé soit "Plusieurs" si il en existe plusieurs dans la database """
    u = get_utilisateur_par_info(nom,prenom)
    if u is []:
        return None
    elif len(u) > 1:
        return "Plusieurs"
    else:
        return u[0]

def get_utilisateur(nom,prenom,mdp): 
    """ Donne l'id utilisateur si les infos sont correctes, si combi n'exisite pas 'Aucun,et si mdp Incorect False'"""

    utilisateur = recherche_utilisateur(nom,prenom)
    if utilisateur is not None:
        if check(mdp,utilisateur["mdp"]):
            return utilisateur["id"]
        else:
            return False
    elif utilisateur == "Plusieurs":
        return "erreur_bd"
    else:
        return "Aucun"
    
def set_utilisateur(nom,prenom,mdp):
    """Essaie de cree un utilisateur et revoie une erreur si besoin sinon False"""
    if recherche_utilisateur(nom,prenom):
        return "Existant"
    elif nom == "" or prenom == "":
        return "Nom/Prenom Vide"
    elif len(mdp) < 7: # 8+ pour un mot de passe robuste
        return "Mdp trop court"
    else:
        ajouter_utilisateur(nom,prenom,crypter(mdp))
        return False
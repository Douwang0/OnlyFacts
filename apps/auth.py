from apps.mdp import crypter, check
from apps.data import recherche_utilisateur,ajouter_utilisateur


def get_utilisateur(nom,prenom,mdp): 
    """ Donne l'id utilisateur si les infos sont correctes, si combi n'exisite pas 'Aucun,et si mdp Incorect False'"""
    utilisateur = recherche_utilisateur(nom,prenom)
    if utilisateur:
        if check(mdp,utilisateur["mdp"]):
            return utilisateur["id"]
        else:
            return False
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
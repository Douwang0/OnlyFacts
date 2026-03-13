import os
from dotenv import load_dotenv

load_dotenv()
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

# TODO : faire la fonction avec de l'encryption
def crypter(mot : str) -> int:
    """Crypte le mdp de facon a ce qu'on ne puisse pas retrouver la var initiale, symetriquement a l'aide de la cle"""
    return hash # PAS SECURE

def check(val, vrai_hash): return crypter(val) == vrai_hash
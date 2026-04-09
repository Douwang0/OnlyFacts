from apps.data import get_posts_avec_infos,get_votes_post
from time import time

def liste_post_fini(fin = 20,croissant=False,cle="created",search=""):
    """Donne la liste des posts prete a etre utiliser dans la page suivant les parametres"""
    posts = get_posts_avec_infos(search)
    for post in posts:
        post["upvote"] = get_votes_post(post["id"])
    posts = tri_selection_dicos_parametre(posts,cle,croissant)
    posts = posts[:fin]
    for post in posts:
        temp = time() - post['created']

        if temp >= 0:
            debut = "Il y a "
        else:
            temp *= -1
            debut = "Dans "

        if temp < 60: # 1min
            post['created'] = f"{int(temp)} sec"
        elif temp < 3600: # 1h
            post['created'] = f"{int(temp//60)} min"
        elif temp < 86400: # 1j
            post['created'] = f"{int(temp//3600)} h"
        elif temp < 31557600: # 1an
            post['created'] = f"{int(temp//86400)} jours"
        else:
            post['created'] = "plus d'un an"
        post['created'] = debut + post['created']

    return posts

def tri_selection_dicos_parametre(liste, cle, croissant): #Terrible pour l'opti avec beaucoup de data mais plus tard sql
    n = len(liste)
    for i in range(n):
        index_extreme = i
        for j in range(i+1, n):
            if croissant:
                if liste[j][cle] < liste[index_extreme][cle]:
                    index_extreme = j
            else:
                if liste[j][cle] > liste[index_extreme][cle]:
                    index_extreme = j
        liste[i], liste[index_extreme] = liste[index_extreme], liste[i]
    return liste
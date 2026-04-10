import sqlite3
from time import time

# REGION INFO TABLE

"""

TABLE users
---
USER_ID INTEGER PRIMARY KEY
FIRST_NAME TEXT
LAST_NAME TEXT
PASSWORD TEXT
---

TABLE posts
---
POST_ID INTEGER PRIMARY KEY
AUTHOR INTEGER
BODY TEXT
DATE TEXT
FOREIGN KEY (AUTHOR) REFERENCES users(USER_ID)
---

TABLE votes
---
USER_VOTE_ID INTEGER
POST_VOTE_ID INTEGER
PRIMARY KEY (USER_VOTE_ID, POST_VOTE_ID)
---

"""

# FIN INFO TABLE

# REGION CORE DATABASE

def ouvrir_database() -> tuple[sqlite3.Connection, sqlite3.Cursor]:

    """
    Renvoie la connection à la database ainsi que son cursor. \n
    -> La connection permet de créer le lien entre le code et la database. \n
    -> Le cursor permet d'executer du code SQL sur la database. \n
    """

    try:
        db_connection : sqlite3.Connection = sqlite3.connect("OF_database.db")
        db_cursor : sqlite3.Cursor = db_connection.cursor()

        return db_connection, db_cursor
    
    except sqlite3.Error as error:
        raise error

def fermer_database(db_connection : sqlite3.Connection) -> None:

    """
    Commit et ferme la connection avec la database. \n
    A utiliser une fois les modifications finies. \n
    """

    try:
        db_connection.commit()
        db_connection.close()

    except sqlite3.Error as error:
        raise error

# FIN CORE DATABASE

# REGION UTILISATEUR

def convert_utilisateur_dict(utilisateur) -> dict:

    """
    Convertie la forme (id,prenom,nom,mdp) de la database en {"id":id,"prenom":prenom,"nom":nom,"mdp":mdp}.
    """

    return {"id":utilisateur[0],"prenom":utilisateur[1],"nom":utilisateur[2],"mdp":utilisateur[3]}

def get_utilisateurs():

    """
    Récupère tous les utilisateurs de la database. \n
    Renvoie une liste de dictionnaire de la forme {"id":id,"prenom":prenom,"nom":nom,"mdp":mdp}. \n
    Renvoie une liste vide s'il n'y en a pas.
    """

    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute("SELECT * FROM users;")
        users = db_cursor.fetchall()
        fermer_database(db_connection)

        l_users : list = []

        for user in users:
            l_users.append(convert_utilisateur_dict(user))

        return l_users

    except sqlite3.Error as error:
        raise error

def get_utilisateur_par_id(id_utilisateur : int) -> dict:

    """
    Renvoie les infos d'un utilisateur à l'aide de son id. \n
    Renvoie un None s'il n'existe pas.
    """
    
    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute(f'SELECT * FROM users WHERE USER_ID={id_utilisateur};')
        user = db_cursor.fetchone()
        fermer_database(db_connection)

        return user if user == None else convert_utilisateur_dict(user)
    
    except sqlite3.Error as error:
        raise error

def get_utilisateur_par_info(prenom, nom):

    """
    Renvoie les infos d'un utilisateur à l'aide de son nom et prénom.\n
    S'il n'y en a aucun, renvoie une liste vide.
    """

    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute(f'SELECT * FROM users WHERE FIRST_NAME=\'{prenom}\' AND LAST_NAME=\'{nom}\'')
        users = db_cursor.fetchall()
        fermer_database(db_connection)

        l_users : list = []

        for user in users:
            l_users.append(convert_utilisateur_dict(user))

        return l_users

    except sqlite3.Error as error:
        raise error

def ajouter_utilisateur(prenom : str, nom : str, mdp):

    """
    Ajoute un nouvel utilisateur dans la table users.
    """
    
    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute(f'INSERT INTO users (FIRST_NAME,LAST_NAME,PASSWORD) VALUES (\'{prenom}\',\'{nom}\',\'{mdp}\');')
        fermer_database(db_connection)
    
    except sqlite3.Error as error:
        raise error

# FIN UTILISATEUR

# REGION POST

def convert_post_dict(post) -> dict:

    """
    Convertie un post de la forme (id,author_id,body,created) en un dictionnaire {"id","author_id","body","created"}.
    """

    return {"id":post[0],"author_id":post[1],"body":post[2],"created":post[3]}

def creer_post(id_utilisateur : int, contenu : str):

    """
    Creer un nouveau post et l'ajoute dans la database.\n
    Le post est rajouté à la table posts.\n
    """
    
    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute(f'INSERT INTO posts (AUTHOR,BODY,DATE) values (\'{id_utilisateur}\',\'{contenu}\',\'{time()}\')')
        fermer_database(db_connection)

    except sqlite3.Error as error:
        raise error

def get_tous_posts():

    """
    Renvoie tous les posts de la table posts sous la forme d'une liste de dictionnaires :\n
    {"id":int,"author_id":int,"body":str,"created":float}\n
    Renvoie une liste vide s'il n'y en a pas.
    """

    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute("SELECT * FROM posts")

        posts = db_cursor.fetchall()
        fermer_database(db_connection)

        l_posts : list = []

        for post in posts:
            l_posts.append(convert_post_dict(post))

        return l_posts
    
    except sqlite3.Error as error:
        raise error
    
def get_posts_avec_infos(texte):
    posts_prepares = []
    posts_avec_mots = rechercher_posts(texte)
    
    for post in posts_avec_mots:

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

def rechercher_posts(texte):

    """
    Renvoie tous les posts similaire à 'texte'.\n
    Renvoie une liste vide s'il n'y en a aucun.
    """
    
    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute(f'SELECT * FROM posts WHERE BODY LIKE \'%{texte}%\';')
        posts = db_cursor.fetchall()
        fermer_database(db_connection)

        l_posts : list = []

        for post in posts:
            l_posts.append(convert_post_dict(post))

        return l_posts
    
    except sqlite3.Error as error:
        raise error

# FIN POST

# REGION VOTE

def utilisateur_a_vote(id_utilisateur, id_post):

    """
    Rajoute un vote de l'utilisateur dans la table votes.
    """

    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute(f'INSERT INTO votes (USER_VOTE_ID,POST_VOTE_ID) values (\'{id_utilisateur}\',\'{id_post}\');')
        fermer_database(db_connection)

    except sqlite3.Error as error:
        raise error
    
# Il faudrait aussi une fonction pour retirer un vote et une fonction pour vérifier si un utilisateur a déjà voté pour un post. TODO

def get_votes_post(id_post):

    """
    Renvoie le nombre de votes qu'a reçu un post.
    """

    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute(f'SELECT COUNT(POST_VOTE_ID) FROM votes WHERE POST_VOTE_ID={id_post};')
        votes = db_cursor.fetchone()[0]
        fermer_database(db_connection)

        return votes
    
    except sqlite3.Error as error:
        raise error

# FIN VOTE

#ajouter_utilisateur([("Prenom", "Nom", hash("MDP"))])
print(get_utilisateurs())
print(get_utilisateur_par_id(1))
print(get_utilisateur_par_info("Charles", "Martinez"))

#creer_post(2, "Ici on aime tous Umamusume.")
print(get_tous_posts())
#utilisateur_a_vote(1,1)
print(get_votes_post(2))


print(get_posts_avec_infos("Umamusume"))

"""
database_connection : sqlite3.Connection | None = None

try:
    database_connection = sqlite3.connect('OF_database.db')
    print("DB Init")
    cursor = database_connection.cursor()

    cursor.execute("DROP TABLE users;")
    cursor.execute("DROP TABLE posts;")
    cursor.execute("DROP TABLE votes;")

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users(" \
        "USER_ID INTEGER PRIMARY KEY," \
        "FIRST_NAME TEXT," \
        "LAST_NAME TEXT," \
        "PASSWORD TEXT" \
        ");"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS posts(" \
        "POST_ID INTEGER PRIMARY KEY," \
        "AUTHOR INTEGER," \
        "BODY TEXT," \
        "DATE TEXT," \
        "FOREIGN KEY (AUTHOR) REFERENCES users(USER_ID)" \
        ");"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS votes(" \
        "USER_VOTE_ID INTEGER," \
        "POST_VOTE_ID INTEGER," \
        "PRIMARY KEY (USER_VOTE_ID, POST_VOTE_ID)" \
        ");"
    )

except sqlite3.Error as error:
    print("SQLite Error - ", error)
"""


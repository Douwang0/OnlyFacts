# Chere charles, ici tu va pouvoir t'amuser

import sqlite3

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

def convert_utilisateur_db_dict(utilisateur) -> dict:

    """
    Convertie la forme (id,prenom,nom,mdp) de la database en {"id":id,"prenom":prenom,"nom":nom,"mdp":mdp}.
    """

    return {"id":utilisateur[0],"prenom":utilisateur[1],"nom":utilisateur[2],"mdp":utilisateur[3]}

def get_utilisateurs():

    """
    Récupère tous les utilisateurs de la database. \n
    Renvoie une liste de dictionnaire de la forme {"id":id,"prenom":prenom,"nom":nom,"mdp":mdp}.
    """

    db_connection, db_cursor = ouvrir_database()

    try:
        db_cursor.execute("SELECT * FROM users;")
        users = db_cursor.fetchall()

        fermer_database(db_connection)

        l_users : list = []

        for user in users:
            l_users.append(convert_utilisateur_db_dict(user))

        return l_users

    except sqlite3.Error as error:
        raise error

def get_utilisateur_par_id(id_utilisateur : int) -> dict:

    """
    Renvoie les infos d'un utilisateur à l'aide de son id. \n
    """
    
    db_connection, db_cursor = ouvrir_database()

    try:
        
        db_cursor.execute(f'SELECT * FROM users WHERE USER_ID={id_utilisateur};')
        user = db_cursor.fetchone()
        fermer_database(db_connection)
        return convert_utilisateur_db_dict(user)
    
    except sqlite3.Error as error:
        raise error

def ajouter_utilisateur(nv_utilisateur):

    """
    Ajoute des nouveaux utilisateurs dans la table users.
    nv_utilisateurs est un tuple de la forme (FIRST_NAME : str, LAST_NAME : str, PASSWORD : hash)
    """
    
    db_connection, db_cursor = ouvrir_database()

    try:
        
        prenom = nv_utilisateur[0]
        nom = nv_utilisateur[1]
        mdp = nv_utilisateur[2]

        db_cursor.execute(f'INSERT INTO users (FIRST_NAME,LAST_NAME,PASSWORD) VALUES (\'{prenom}\',\'{nom}\',\'{mdp}\');')

        fermer_database(db_connection)
    
    except sqlite3.Error as error:
        raise error
    
#ajouter_utilisateur([("Prenom", "Nom", hash("MDP"))])
print(get_utilisateurs())
print(get_utilisateur_par_id(1))

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

db_test_user = [
    {"id": 1, "nom": "admin", "prenom": "admin", "mdp": "vous_ne_saurez_jamais"},
    {"id": 2, "nom": "Villermaux-Natalini", "prenom": "Giulian", "mdp": "3.1415926"},
    {"id": 3, "nom": "Dupont", "prenom": "Alice", "mdp": "bonjour123"},
    {"id": 4, "nom": "Martin", "prenom": "Lucas", "mdp": "password"},
    {"id": 5, "nom": "Durand", "prenom": "Emma", "mdp": "chienchat"},
    {"id": 6, "nom": "Bernard", "prenom": "Hugo", "mdp": "azerty"},
    {"id": 7, "nom": "Petit", "prenom": "Chloe", "mdp": "soleil"},
    {"id": 8, "nom": "Tom", "prenom": "falz", "mdp": "motdepasse"}
]

db_test_posts = [
    {
        "id": 1,
        "author_id": 2,
        "body": "Finally got my Flask login system working!",
        "created": 1773475320
    },
    {
        "id": 2,
        "author_id": 3,
        "body": "Just finished reading a great sci-fi novel.",
        "created": 1773478200
    },
    {
        "id": 3,
        "author_id": 4,
        "body": "Python imports are confusing at first but they start making sense.",
        "created": 1773548700
    },
    {
        "id": 4,
        "author_id": 5,
        "body": "Beautiful sunset today near the beach.",
        "created": 1773573720
    },
    {
        "id": 5,
        "author_id": 2,
        "body": "Coffee + coding = perfect afternoon.",
        "created": 1773656520
    },
    {
        "id": 6,
        "author_id": 6,
        "body": "Trying to learn SQL and relational databases.",
        "created": 1773659100
    },
    {
        "id": 7,
        "author_id": 7,
        "body": "Anyone else procrastinating instead of studying?",
        "created": 1773664380
    },
    {
        "id": 8,
        "author_id": 1,
        "body": "Server maintenance tonight, expect downtime around 2am.",
        "created": 1773666900
    }
]

db_test_votes = [
    {"user_id": 1, "post_id": 1},
    {"user_id": 3, "post_id": 1},
    {"user_id": 4, "post_id": 1},

    {"user_id": 2, "post_id": 2},
    {"user_id": 5, "post_id": 2},

    {"user_id": 1, "post_id": 3},
    {"user_id": 2, "post_id": 3},
    {"user_id": 6, "post_id": 3},

    {"user_id": 3, "post_id": 4},
    {"user_id": 4, "post_id": 4},
    {"user_id": 7, "post_id": 4},

    {"user_id": 1, "post_id": 5},
    {"user_id": 5, "post_id": 5},

    {"user_id": 2, "post_id": 6},
    {"user_id": 3, "post_id": 6},
    {"user_id": 4, "post_id": 6},

    {"user_id": 6, "post_id": 7},

    {"user_id": 2, "post_id": 8},
    {"user_id": 3, "post_id": 8},
    {"user_id": 4, "post_id": 8},
    {"user_id": 5, "post_id": 8}
]
        

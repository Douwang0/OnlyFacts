# Chere charles, ici tu va pouvoir t'amuser

import sqlite3

database_connection : sqlite3.Connection | None = None

try:
    database_connection = sqlite3.connect('OF_database.db')
    print("DB Init")
    cursor = database_connection.cursor()

    cursor.execute('SELECT sqlite_version();')
    result = cursor.fetchall()

    print("SQL Version : {}".format(result[0][0]))

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users(" \
        "USER_ID INT PRIMARY KEY," \
        "FIRST_NAME TEXT," \
        "SURNAME TEXT," \
        "PASSWORD TEXT" \
        ");"
    )

    cursor.execute(
        f"INSERT INTO users VALUES (0, 'Villermaux-Natalini', 'Giulian', '{hash("vous_ne_saurez_jamais")}');"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS posts(" \
        "POST_ID INT PRIMARY KEY," \
        "AUTHOR INT," \
        "BODY TEXT," \
        "DATE TEXT," \
        "FOREIGN KEY (AUTHOR) REFERENCES users(USER_ID)" \
        ");"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS votes(" \
        "USER_VOTE_ID INT," \
        "POST_VOTE_ID INT," \
        "PRIMARY KEY (USER_VOTE_ID, POST_VOTE_ID)" \
        ");"
    )

    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    print(users)

except sqlite3.Error as error:
    print("SQLite Error - ", error)

finally:
    if database_connection:
        database_connection.close()
        print("DB Connection closed")

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
        

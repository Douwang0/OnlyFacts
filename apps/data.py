db_test_votes = []

def utilisateur_a_vote(id_utilisateur, id_post):
    for vote in db_test_votes:
        if vote["user_id"] == id_utilisateur and vote["post_id"] == id_post:
            return True
    return False

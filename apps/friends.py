from db import est_ami, get_tous_les_amis

def get_lien_minimum(id_utilisateur, id_personne):

    """
    Renvoie une liste d'id utilisateurs formant le plus court chemin entre
    deux personnes par les liens d'amitiés qu'elles ont.
    """

    if est_ami(id_utilisateur, id_personne): return [id_personne]

    found_person : bool = False

    path : list[int] = []
    queue : list[int] = [id_utilisateur]
    parents : dict = {id_utilisateur : None}

    while queue != [] and not found_person:

        current_id : int = queue.pop(0)
        friends : list = get_tous_les_amis(current_id)

        for friend in friends:

            if friend in parents.keys():
                continue

            parents[friend] = current_id

            if  friend == id_personne:
                found_person = True
                break
            
            queue.append(friend)

    if found_person:

        path.append(id_personne)
        path_completed : bool = False

        while not path_completed:

            parent : int = parents[path[-1]]

            if parent == None:
                path_completed = True
                continue

            path.append(parent)
        
        return path[::-1]
    
    return []
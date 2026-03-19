
# - Historique des modifications -

- 12/03/26 Giulian : Template vide (info debut)
- 18/03/26 Finission du Cahier initial

# - En-Tête -

Nom de l'équipe : M.I.G.A (Make information great again)
Membres : Charles, Giulian, Tom, Nathan
Rôles : 
- Charles : Backend, Base de donnée
- Giulian : Fullstack, Implementation Lien Python Html et Logique, Chef de projet
- Tom : Frontend
- Nathan : Frontend
Titre du projet : OnlyFacts
Date de début : 12/03/26

## 1. Objectif

Développer une application web permettant à des utilisateurs de publier et consulter des messages, avec un système de compte et d’interactions.

---

## 2. Gestion des utilisateurs

Le système doit permettre :

- la création de compte (nom, prénom, mot de passe)
    
- la connexion à un compte existant
    
- le maintien de la session utilisateur
    
- la déconnexion
    

---

## 3. Gestion des posts

Le système doit permettre :

- la création de posts
    
- l’affichage de tous les posts
    
- l’affichage des informations suivantes :
    
    - auteur
        
    - date
        
    - nombre de votes
        

---

## 4. Système de votes

Le système doit permettre :

- de voter pour un post
    
- d’empêcher un utilisateur de voter plusieurs fois pour le même post
    

---

## 5. Tri et affichage

Le système doit permettre :

- de trier les posts selon :
    
    - la date
        
    - le nombre de votes
        
- de choisir :
    
    - ordre croissant
        
    - ordre décroissant
        

---

## 6. Interface

Le site doit proposer :

- une page d’accueil (posts)
    
- une page de connexion
    
- une page d’inscription
    
- une navigation simple entre les pages
    

---

## 7. Contraintes techniques

- utilisation de Flask
    
- utilisation de templates HTML
    
- gestion des données côté serveur
    
- structure de projet claire et modulaire
    

---

## 8. Sécurité

Le système doit :

- sécuriser les mots de passe
    
- valider les entrées utilisateur
    
- protéger les sessions
    

---

## 9. Gestion des données

Le système doit :

- stocker les utilisateurs
    
- stocker les posts
    
- permettre une évolution vers une base de données persistante
    

---

## 10. Performance

Le système doit :

- gérer efficacement le tri des posts
    
- rester performant avec un grand nombre de données

# TP 1 : Classes et Objets


# Exercice 1 — Compteur de visites de pages

 **Objectif :** distinguer attribut de classe et attribut d’instance.

---

##  Description
La classe `CompteurPage` permet de suivre le nombre total de visites sur plusieurs pages.
Chaque page possède une URL unique, mais le compteur global est partagé par toutes les instances.

---

##  Structure
- `compteur_page.py` → contient la classe `CompteurPage`
- `test_compteur_page.py` → script de test

---

## Sortie attendue :
```
Page https://example.com/ — visites globales : 3
Page https://example.com/blog — visites globales : 3
Page https://example.com/contact — visites globales : 3
Total global attendu : 3

Visites par page :
https://example.com/ → 2 lectures
https://example.com/blog → 1 lectures
https://example.com/contact → 0 lectures
```
##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :


<img width="819" height="287" alt="image" src="https://github.com/user-attachments/assets/da8eebd8-4a90-4713-98b2-604ef9a52d02" />

---

# Exercice 2 — Gestion d’inventaire d’articles

**Objectif :** 
encapsuler données métier et calculs.

##  Description
La classe `Article` représente un produit en stock avec ses informations : référence, désignation, prix HT et quantité disponible.


##  Structure
- `article.py` → classe `Article`
- `inventaire.py` → script principal de test
- `mouvements.log` → journal des approvisionnements

## Sortie attendue :
```
Réf A101 — Clavier mécanique : 10 unités à 59.9 € HT
Réf A102 — Souris sans fil : 25 unités à 29.5 € HT
Réf A103 — Écran 24 pouces : 5 unités à 189.0 € HT

Valeur d’inventaire : 2281.50 €

Après approvisionnement :
Réf A101 — Clavier mécanique : 15 unités à 59.9 € HT
Réf A102 — Souris sans fil : 25 unités à 29.5 € HT
Réf A103 — Écran 24 pouces : 7 unités à 189.0 € HT
```

##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="826" height="326" alt="image" src="https://github.com/user-attachments/assets/61b817c2-1ec3-4905-b685-ae5be1e1eb28" />

---

# Exercice 3 — Carnet d’adresses minimal

 **Objectif :**
 travailler avec listes d’objets, propriétés et recherche.

## Description
La classe `Contact` stocke les informations d’une personne (nom, téléphone, email).  
La classe `Carnet` permet d’ajouter, rechercher et afficher des contacts.

---

##  Structure
- `contact.py` → classe `Contact`
- `carnet.py` → classe `Carnet`
- `test_carnet.py` → script de démonstration

## Sortie attendue :
```
=== Tous les contacts ===
Amina Saidi — 0612345678 — amina@example.com
Youssef Belkhou — 0699988877 — youssef@example.com
Said Toumi — 0677001122 — said@example.com

=== Résultat de recherche : 'sa' ===
Amina Saidi 0612345678
Said Toumi 0677001122

Nombre total de contacts : 3
```
##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :


<img width="737" height="317" alt="image" src="https://github.com/user-attachments/assets/569f5a69-d68b-41fb-b8c8-97db5cbaa606" />

---

# Exercice 4 — Calculatrice géométrique pour cercles

 **Objectif :** 
 sécuriser l’accès aux attributs avec des propriétés.

---

## Description
La classe `Cercle` calcule le **périmètre** et la **surface** d’un cercle tout en contrôlant la validité du rayon.

---

##  Structure
- `cercle.py` → classe `Cercle`
- `test_cercle.py` → script de test

---

## Sortie attendue :
```
Périmètre : 18.85
Surface   : 28.27
Erreur capturée : Le rayon doit être strictement positif.       

--- Test agrandissement ---
Nouveau rayon : 4.5
Nouvelle surface : 63.62
```

##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="804" height="233" alt="image" src="https://github.com/user-attachments/assets/8ab6fdae-7983-43b0-a5d5-4e102311f34b" />

---

# Exercice 5 — Journal de tâches avec gestion de contexte

 **Objectif :** 
 exploiter `with` pour ouvrir et fermer automatiquement un fichier.

##  Description
La classe `JournalTaches` gère un fichier texte `journal.txt` pour enregistrer les tâches avec leur date et heure.

---

##  Structure
- `journal.py` → classe `JournalTaches`

---

## Sortie attendue :
```
--- Contenu du journal ---
=== Historique des tâches (plus récentes en haut) ===
[2025-11-07 15:35:34] Envoyer le rapport hebdomadaire
[2025-11-07 15:35:33] Faire la revue de code
[2025-11-07 15:35:32] Préparer la réunion du projet X
[2025-11-07 15:00:58] Envoyer le rapport hebdomadaire
[2025-11-07 15:00:57] Faire la revue de code
[2025-11-07 15:00:56] Préparer la réunion du projet X
```
##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="885" height="272" alt="image" src="https://github.com/user-attachments/assets/6d16d511-6f95-406f-8976-46c728c6af59" />

---


# Exercice 6 — Convertisseur de devises

 **Objectif :**
illustrer les méthodes statiques et de classe.

---

##  Description
La classe `Convertisseur` permet de convertir des montants entre **euros** et **dirhams marocains (DH)**.

---

##  Structure
- `convertisseur.py` → classe `Convertisseur`
- `test_convertisseur.py` → script de test

---

## Sortie attendue :
```
Avant mise à jour : 1090.0
Après mise à jour  : 1120.0

560 DH = 50.00 EUR au taux actuel (11.2)
```
##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="666" height="138" alt="image" src="https://github.com/user-attachments/assets/71f15ef1-3a03-40c8-863a-5d87d2c14d24" />





from carnet import Carnet
from contact import Contact

# Création du carnet
c = Carnet()

# Ajout de quelques contacts
c.ajouter(Contact("Amina Saidi", "0612345678", "amina@example.com"))
c.ajouter(Contact("Youssef Belkhou", "0699988877", "youssef@example.com"))
c.ajouter(Contact("Said Toumi", "0677001122", "said@example.com"))

# Affichage complet
print("=== Tous les contacts ===")
c.afficher_tous()

# Recherche d’un fragment
print("\n=== Résultat de recherche : 'sa' ===")
resultat = c.recherche("sa")
for contact in resultat:
    print(contact.nom, contact.telephone)

# Vérification de la propriété nombre_contacts
print(f"\nNombre total de contacts : {c.nombre_contacts}")

from convertisseur import Convertisseur

montant = 100

print("Avant mise à jour :", Convertisseur.vers_dh(montant))

# Mise à jour du taux
Convertisseur.mettre_a_jour_taux(11.2)
print("Après mise à jour  :", Convertisseur.vers_dh(montant))

# Test de la méthode vers_eur (extension)
dirhams = 560
euros = Convertisseur.vers_eur(dirhams)
print(f"\n{dirhams} DH = {euros:.2f} EUR au taux actuel ({Convertisseur.taux_eur_dh})")

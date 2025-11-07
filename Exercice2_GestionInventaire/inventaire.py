from article import Article

# Création de trois articles
a1 = Article("A101", "Clavier mécanique", 59.90, 10)
a2 = Article("A102", "Souris sans fil", 29.50, 25)
a3 = Article("A103", "Écran 24 pouces", 189.00, 5)

articles = [a1, a2, a3]

# Affichage de chaque article
for a in articles:
    print(a)

# Calcul de la valeur totale du stock
total = sum(a.valeur_stock() for a in articles)
print(f"\nValeur d’inventaire : {total:.2f} €")

# Exemple d’approvisionnement (optionnel)
a1.approvisionner(5)
a3.approvisionner(2)

print("\nAprès approvisionnement :")
for a in articles:
    print(a)

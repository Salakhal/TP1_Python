from compteur_page import CompteurPage

p1 = CompteurPage("https://example.com/")
p2 = CompteurPage("https://example.com/blog")
p3 = CompteurPage("https://example.com/contact")

for p in (p1, p2, p3):
    print(p.afficher_stats())

# Vérification du compteur global
print("Total global attendu :", CompteurPage.total_visites)

# Test de la méthode enregistrer_lecture()
p1.enregistrer_lecture()
p1.enregistrer_lecture()
p2.enregistrer_lecture()

print(f"\nVisites par page :")
print(f"{p1.url} → {p1.visites_par_page} lectures")
print(f"{p2.url} → {p2.visites_par_page} lectures")
print(f"{p3.url} → {p3.visites_par_page} lectures")

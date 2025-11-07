from cercle import Cercle
from math import pi

c = Cercle(3)
print(f"Périmètre : {c.perimetre:.2f}")  # 2πr
print(f"Surface   : {c.surface:.2f}")    # πr²

# Test du contrôle d'erreur
try:
    c.rayon = -5
except ValueError as e:
    print("Erreur capturée :", e)

# Test de la méthode agrandir
print("\n--- Test agrandissement ---")
c.agrandir(50)  # +50%
print(f"Nouveau rayon : {c.rayon}")
print(f"Nouvelle surface : {c.surface:.2f}")

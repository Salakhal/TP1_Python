from math import pi

class Cercle:
    def __init__(self, rayon: float):
        # Utilisation du setter pour appliquer le contrôle dès la création
        self.rayon = rayon

    @property
    def rayon(self) -> float:
        """Retourne la valeur actuelle du rayon"""
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        """Contrôle de validité du rayon"""
        if valeur <= 0:
            raise ValueError("Le rayon doit être strictement positif.")
        self._rayon = valeur

    @property
    def perimetre(self) -> float:
        """Retourne le périmètre du cercle (2πr)"""
        return 2 * pi * self._rayon

    @property
    def surface(self) -> float:
        """Retourne la surface du cercle (πr²)"""
        return pi * self._rayon ** 2

    def agrandir(self, pourcentage: float):
        """Augmente le rayon de p %"""
        if pourcentage < -100:
            raise ValueError("La réduction ne peut pas dépasser 100 % du rayon.")
        self._rayon *= (1 + pourcentage / 100)

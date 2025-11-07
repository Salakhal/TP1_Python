class Contact:
    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    @property
    def initial(self) -> str:
        """Retourne la première lettre du nom en majuscule"""
        return self.nom[0].upper()

    def __str__(self) -> str:
        """Affichage lisible d’un contact"""
        return f"{self.nom} — {self.telephone} — {self.email}"

from contact import Contact

class Carnet:
    def __init__(self):
        # Attribut privé : liste de contacts
        self._contacts = []

    def ajouter(self, contact: Contact):
        """Ajoute un contact au carnet"""
        self._contacts.append(contact)

    def recherche(self, fragment: str):
        """Retourne les contacts dont le nom contient le fragment (insensible à la casse)"""
        fragment = fragment.lower()
        return [c for c in self._contacts if fragment in c.nom.lower()]

    def afficher_tous(self):
        """Affiche tous les contacts du carnet"""
        for c in self._contacts:
            print(c)

    @property
    def nombre_contacts(self) -> int:
        """Propriété en lecture seule : nombre total de contacts"""
        return len(self._contacts)

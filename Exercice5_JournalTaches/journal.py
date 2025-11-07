from datetime import datetime

class JournalTaches:
    def __enter__(self):
        """Ouvre le fichier journal.txt en mode ajout et retourne l'objet courant."""
        self._fichier = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        """Écrit une tâche avec l'horodatage ISO dans le journal."""
        horodatage = datetime.now().isoformat(sep=" ", timespec="seconds")
        self._fichier.write(f"[{horodatage}] {tache}\n")

    def __exit__(self, exc_type, exc, tb):
        """Ferme le fichier automatiquement à la sortie du bloc with."""
        self._fichier.close()

    @classmethod
    def lire(cls):
        """Affiche l'historique des tâches dans l'ordre chronologique inverse."""
        try:
            with open("journal.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
                if not lignes:
                    print("Aucune tâche enregistrée.")
                    return
                print("=== Historique des tâches (plus récentes en haut) ===")
                for ligne in reversed(lignes):
                    print(ligne.strip())
        except FileNotFoundError:
            print("Aucun fichier journal trouvé.")

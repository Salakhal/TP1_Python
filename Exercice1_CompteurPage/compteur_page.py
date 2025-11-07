class CompteurPage:
    # Attribut de classe
    total_visites = 0

    def __init__(self, url: str):
        # Attribut d’instance
        self.url = url
        self.visites_par_page = 0

        # Incrémentation de l’attribut de classe
        CompteurPage.total_visites += 1

    def afficher_stats(self) -> str:
        """Retourne les statistiques globales"""
        return f"Page {self.url} — visites globales : {CompteurPage.total_visites}"

    def enregistrer_lecture(self):
        """Incrémente le nombre de visites pour cette page"""
        self.visites_par_page += 1

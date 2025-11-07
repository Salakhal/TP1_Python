class Convertisseur:
    # Attribut de classe : taux de conversion EUR → DH
    taux_eur_dh = 10.9

    @staticmethod
    def vers_dh(euros: float) -> float:
        """Convertit un montant en euros vers dirhams."""
        return euros * Convertisseur.taux_eur_dh

    @staticmethod
    def vers_eur(dirhams: float) -> float:
        """Convertit un montant en dirhams vers euros (extension)."""
        return dirhams / Convertisseur.taux_eur_dh

    @classmethod
    def mettre_a_jour_taux(cls, nv_taux: float):
        """Met à jour le taux de conversion."""
        if nv_taux <= 0:
            raise ValueError("Le taux doit être strictement positif.")
        cls.taux_eur_dh = nv_taux

class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        
        return self.prix_ht * self.stock

    def __str__(self) -> str:
         return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht} € HT"

    def approvisionner(self, qte: int):
        if qte <= 0:
            raise ValueError("La quantité d’approvisionnement doit être positive.")
        self.stock += qte

        with open("mouvements.log", "a", encoding="utf-8") as f:
            f.write(f"Approvisionnement de {qte} unités pour {self.designation} (Réf {self.reference})\n")

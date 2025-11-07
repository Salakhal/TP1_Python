from journal import JournalTaches
from time import sleep

# Enregistrement de quelques tâches dans le journal
with JournalTaches() as journal:
    journal.enregistrer("Préparer la réunion du projet X")
    sleep(1)
    journal.enregistrer("Faire la revue de code")
    sleep(1)
    journal.enregistrer("Envoyer le rapport hebdomadaire")

# Lecture du journal complet
print("\n--- Contenu du journal ---")
JournalTaches.lire()

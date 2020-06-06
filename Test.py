import time
import Utilitaire

# Résumé :
if __name__ == '__main__':
    temps_debut = time.time_ns()

    # CODE ICI

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(-1, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : -1 , en : -1 ms.

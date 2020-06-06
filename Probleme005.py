import time
import Utilitaire
import math

# Résumé: On trouve le PPCM des nombres de 2 à 20.
# Pour se faire, on décompose les nombres composés (non premier) en multiples de premiers.
# Exemple : 6 n'est pas présent, car 2 et 3 le sont (6 = 2 * 3).
if __name__ == '__main__':
    temps_debut = time.time_ns()

    multiples = int(math.pow(2, 4) * math.pow(3, 2) * 5 * 7 * 11 * 13 * 17 * 19)  # PPCM des nombres de 2 à 20

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(multiples, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 232792560 , en : 0 ns.

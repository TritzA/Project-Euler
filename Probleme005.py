import time

import Uti

# Résumé: On trouve le PPCM des nombres de 2 à 20.
# Pour se faire, on décompose les nombres composés (non premier) en multiples de premiers.
# Exemple : 6 n'est pas présent, car 2 et 3 le sont (6 = 2 * 3).
if __name__ == '__main__':
    temps_debut = time.time()

    multiples = 2 ** 4 * 3 ** 2 * 5 * 7 * 11 * 13 * 17 * 19  # PPCM des nombres de 2 à 20

    temps_fin = time.time()
    Uti.rep(multiples, temps_fin - temps_debut)
    # Réponse : 232792560 , en : 0.000 s.

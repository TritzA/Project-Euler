import time

import numpy as np

from Utilitaire import Gene

# Résumé : Les problèmes 31, 76 et 77 sont presque les mêmes, voir problème 31 pour une meilleure explication.
if __name__ == '__main__':
    temps_debut = time.time()

    somme = 100
    pieces = []
    for i in range(1, somme + 1):
        pieces.append(i)
    cmpt = np.zeros(somme + 1)
    cmpt[0] = 1

    for i in range(0, len(pieces)):
        for j in range(pieces[i], somme + 1):
            cmpt[j] += cmpt[
                j - pieces[i]]

    temps_fin = time.time()
    Gene.rep(int(cmpt[-1]), temps_fin - temps_debut)
    # Réponse : 190569292 , en : 0.003 s.

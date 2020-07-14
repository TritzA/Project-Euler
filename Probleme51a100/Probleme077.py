import time

import numpy as np

from Utilitaire import Gene
from Utilitaire import Nb

# Résumé : Les problèmes 31, 76 et 77 sont presque les mêmes, voir problème 31 pour une meilleure explication.
if __name__ == '__main__':
    temps_debut = time.time()

    trouve = False
    pieces = []
    somme = 2
    while not trouve:
        if Nb.premier(somme):  # si l'on rencontre un nombre premier, on l'ajoute à la liste
            pieces.append(somme)
        somme += 1  # puis on roule l'équivalent du problème 76 pour le nombre suivant

        cmpt = np.zeros(somme + 1)
        cmpt[0] = 1

        for i in range(0, len(pieces)):
            for j in range(pieces[i], somme + 1):
                cmpt[j] += cmpt[j - pieces[i]]
        if int(cmpt[-1]) > 5000:
            trouve = True

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 71 , en : 0.015 s.

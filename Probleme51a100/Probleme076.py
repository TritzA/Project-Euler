import math
import time

from Utilitaire import Gene


def p(n):
    produit = 1
    for i in range(1, 100):
        produit *= 1 / (1 - math.pow(n, i))
    return produit

# Résumé :
if __name__ == '__main__':
        temps_debut = time.time()

        partition = p(100)

        temps_fin = time.time()
        Gene.rep(partition, temps_fin - temps_debut)
        # Réponse : -1 , en : -1 s.
        # rep 190 569 292

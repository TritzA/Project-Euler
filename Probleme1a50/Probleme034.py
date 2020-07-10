import math
import time

from Utilitaire import Gene


def facto_chiffres(n):
    somme = 0
    for i in str(n):
        somme += math.factorial(int(i))
    if n == somme:
        return True
    else:
        return False


# Résumé : On passe à travers les nombres de 3 à 100000 exclusivement.
# Puis, on incrémente la somme les nombres dont le factoriel des chiffres
# qui le compose est égale au nombre lui-même.
if __name__ == '__main__':
    temps_debut = time.time()

    somme = 0
    i = 3
    while i < 100000:
        i += 1
        if facto_chiffres(i):
            somme += i

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 40730 , en : 3.140 s.

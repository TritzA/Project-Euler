import time
from itertools import permutations

from Utilitaire import Nb, Gene


def converstion_tuple(tup):
    chaine = ''.join(tup)
    return chaine


# Résumé : En partant des pandigitals de rend n, on diminue jusqu'à trouver un nombre premier.
# Pour chaque nombre de taille n, on parcourt toutes les permutations en ordre croissant en
# testant si elles sont éléments des nombres premiers.
if __name__ == '__main__':
    temps_debut = time.time()

    chaine = "123456789*"
    perm = permutations(chaine)

    max = 0
    while max == 0: # tant qu'on a pas trouvé
        chaine = chaine[:len(chaine) - 1]
        perm = permutations(chaine)
        max = 0

        for i in perm: # parcours toutes les permutations de pandigitals
            i = int(converstion_tuple(i))
            if Nb.premier(i): # la liste étant en ordre croissant, le dernier trouvé est forcément le plus grand
                max = i

    temps_fin = time.time()
    Gene.rep(max, temps_fin - temps_debut)
    # Réponse : 7652413 , en : 0.691 s.

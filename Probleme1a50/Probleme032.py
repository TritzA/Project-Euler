import time
from itertools import permutations

from Utilitaire import Gene


def converstion_tuple(tup):
    chaine = ''.join(tup)
    return chaine


# Résumé : On parcourt toutes les permutations possibles de "123456789",
# puis on sépare chaque permutation en une expression. Si l'expression est vraie,
# on ajoute le produit à l'ensemble des pandigitals. On termine en sommant l'ensemble.
if __name__ == '__main__':
    temps_debut = time.time()

    pandigitals = set()
    chaine = "123456789"
    perm = permutations(chaine)

    for i in list(perm):
        i = converstion_tuple(i)

        for coupure_a in range(1, len(i) - 1):
            a = str(i[:coupure_a])
            coupure_b = coupure_a + 1

            for coupure_b in range(coupure_a + 1, len(i)):
                b = str(i[coupure_a:coupure_b])

                if int(a) * int(b) == int(i[coupure_b:]):
                    pandigitals.add(int(i[coupure_b:]))

    somme_produit = sum(pandigitals)

    temps_fin = time.time()
    Gene.rep(somme_produit, temps_fin - temps_debut)
    # Réponse : 45228 , en : 23.050 s.

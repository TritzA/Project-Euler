import time
from itertools import permutations

from Utilitaire import Gene

premiers = [2, 3, 5, 7, 11, 13, 17]


def converstion_tuple(tup):
    chaine = ''.join(tup)
    return chaine


def propriete(chaine):
    bon = True
    i = 1
    while i < 8 and bon:
        tempo = int(chaine[i] + chaine[i + 1] + chaine[i + 2])
        if tempo % premiers[i - 1] != 0:
            return False
        i += 1
    return bon


# Résumé : On teste si chacune des permutations respecte la propriété.
# Si c'est le cas, on ajoute ce nombre à la somme.
if __name__ == '__main__':
    temps_debut = time.time()

    chaine = "0123456789"
    perm = permutations(chaine)
    somme = 0

    for element in perm:
        if propriete(element):
            somme += int(converstion_tuple(element))

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 16695334890 , en : 10.854 s.

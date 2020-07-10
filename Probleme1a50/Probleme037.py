import time

from Utilitaire import Nb, Gene


def decompose(n):
    n = str(n)
    premiers = set()
    for i in range(1, len(n)):
        premiers.add(n[:i])
    for i in range(1, len(n)):
        if not n[i:] in premiers:
            premiers.add(n[i:])
    return premiers


# Résumé : Tant qu'on n'a pas trouvé les 11 premiers, on décompose les nombres premiers
# trouvés en testant si l'ensemble de leur décomposition est aussi premier.
if __name__ == '__main__':
    temps_debut = time.time()

    trouve = False
    i = 11
    premiers = [2, 3, 5, 7]
    somme = 0
    cmpt = 0

    while cmpt < 11:

        if Nb.premier(i):
            premiers.append(i)  # on conserve les nombres premiers quand on les trouve

            premiers_tronque = decompose(i)
            bon = True
            for element in premiers_tronque:  # ajout beak a la main
                if not Nb.premier(int(element)):
                    bon = False
            if bon:
                cmpt += 1
                somme += i
        i += 2

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 748317 , en : 8.437 s.

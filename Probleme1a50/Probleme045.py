import time

from Utilitaire import Nb, Gene


def H(n):
    return n * (2 * n - 1)


# Résumé : "Ainsi, les nombres hexagonaux sont simplement les nombres triangulaires d'indices impairs." - Wikipédia
# On cherche un nombre issu de l'intersection entre les nombres triangulaires, pentagonaux et hexagonaux.
# Les nombres hexagonaux sont un sous-ensemble des nombres triangulaires,
# nous n'avons donc qu'à trouver l'intersection entre les nombres hexagonaux et pentagonaux.
# On parcourt donc les nombres hexagonaux grâce à leur indice en testant
# à chaque fois grâce à un test simple s'ils sont aussi élément des nombres pentagonaux.
if __name__ == '__main__':
    temps_debut = time.time()

    trouve = False
    i = 143
    while not trouve:
        i += 1
        hexa = H(i)
        if Nb.pentagonal(hexa):
            trouve = True

    temps_fin = time.time()
    Gene.rep(hexa, temps_fin - temps_debut)
    # Réponse : 1533776805 , en : 0.035 s.

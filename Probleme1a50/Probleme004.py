import time

from Utilitaire import Nb, Gene


def decomposition_facteur_possible(nb):
    decomposable = False
    j = 999
    while j > 99 and not decomposable:
        if nb % j == 0:
            if len(str((nb // j))) == 3:  # ou pas entiere
                decomposable = True
        j -= 1
    return decomposable


# Résumé : En partant du plus gros nombre possible,
# on cherche un nombre qui est à la fois et palindrome
# et décomposable en deux facteurs composés de trois chiffres.
if __name__ == '__main__':
    temps_debut = time.time()

    trouve = False
    i = 999 * 999 + 1

    while not trouve:
        i -= 1
        if Nb.palindrome(i):
            if decomposition_facteur_possible(i):
                trouve = True

    temps_fin = time.time()
    Gene.rep(i, temps_fin - temps_debut)
    # Réponse : 906609 , en : 0.129 s.

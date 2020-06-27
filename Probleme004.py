import time
import Uti
import Nb


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
    i = 999 * 999

    while not trouve:
        if Nb.palindrome(i):
            if decomposition_facteur_possible(i):
                trouve = True
            else:
                i -= 1
        else:
            i -= 1

    temps_fin = time.time()
    Uti.rep(i, temps_fin - temps_debut)
    # Réponse : 906609 , en : 0.129 s.

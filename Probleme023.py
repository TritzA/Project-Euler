import time

import Nb
import Uti


def est_somme_abon(somme, liste):
    i = 0
    while i != len(liste) // 2:
        terme = liste[i]
        complement = somme - terme
        if Uti.binary_search(liste, i, len(liste), complement) != -1:
            return True
        i += 1
    return False


# Résumé : On liste tous les nombres abondants inférieurs à 28123 dans une liste.
# Puis, si un nombre entre 1 et 28123 ne peut être écrit comme la somme de cette liste, l'incrémenter à la somme.
if __name__ == '__main__':
    temps_debut = time.time()

    abon = [i for i in range(2, 28123) if Nb.abondant(i)]

    somme = 0
    for i in range(1, 28123):
        if not est_somme_abon(i, abon):
            somme += i

    temps_fin = time.time()
    Uti.rep(somme, temps_fin - temps_debut)
    # Réponse : 4179871 , en : 71.007 s.

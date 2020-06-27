import time
import Uti
import math

objectif = 1000000


def permutations(tab, debut):
    taille = len(tab)
    if taille == 1:  # se termine si on a tout utilisé
        return tab
    max = math.factorial(taille)  # trouve le maximum de combinaisons possible

    somme = debut
    cmpt = -1
    bonds = max // taille
    while somme < objectif:
        somme += bonds
        cmpt += 1

    somme -= (max // taille)
    chiffre = str(tab[cmpt])
    tab = tab.replace(chiffre, '')

    return chiffre + permutations(tab, somme)


# Résumé : On détermine les chiffres de gauche à droite grâce à une fonction récursive
# qui se prolonge à chaque fois qu'elle est à une itération de dépasser l'objectif.
# Elle s'arrête définitivement lorsqu'il ne lui reste que le dernier chiffre à placer.
if __name__ == '__main__':
    temps_debut = time.time()

    tab = "0123456789"
    reponse = permutations(tab, 0)

    temps_fin = time.time()
    Uti.rep(reponse, temps_fin - temps_debut)
    # Réponse : 2783915460 , en : 0.000 s.

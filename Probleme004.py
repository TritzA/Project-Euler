import time
import math


def fin_temps(temps_fin, temps_debut):
    return (temps_fin - temps_debut) / math.pow(10, 6)


def est_Palindrome(nb):
    chaine_nb = str(nb)
    i = 0
    palindrome = True
    while i < int(len(chaine_nb) / 2) + 1 and palindrome:
        if chaine_nb[i] != chaine_nb[len(chaine_nb) - (i + 1)]:
            palindrome = False
        i += 1
    return palindrome


def decomposition_facteur_possible(nb):
    decomposition = False
    i = 999
    while i > 99 and not decomposition:
        if nb % i == 0 and len((str(int(nb / i)))) == 3:
            decomposition = True
        i -= 1
    return decomposition


# Résumé : En partant du plus gros nombre possible,
# on cherche un nombre qui est à la fois et palindrome
# et décomposable en deux facteurs composés de trois chiffres.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    trouve = False
    iterateur = 999 * 999

    while not trouve:
        if est_Palindrome(iterateur) and decomposition_facteur_possible(iterateur):
            trouve = True
        else:
            iterateur -= 1

    temps_fin = time.time()
    reponse = iterateur
    print("Réponse :", reponse, ", en :", fin_temps(temps_fin, temps_debut), "ms.")
    # Réponse : 906609 , en : 206.4501 ms.

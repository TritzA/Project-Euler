import time
import Utilitaire


def est_Palindrome(nb):
    chaine_nb = str(nb)
    k = 0
    palindrome = True
    while k < len(chaine_nb) // 2 and palindrome:
        if chaine_nb[k] != chaine_nb[len(chaine_nb) - (k + 1)]:
            palindrome = False
        k += 1
    return palindrome


def decomposition_facteur_possible(nb):
    decomposable = False
    j = 999
    while j > 99 and not decomposable:
        if nb % j == 0:
            if Utilitaire.taille(nb // j) == 3:  # ou pas entiere
                decomposable = True
        j -= 1
    return decomposable


# Résumé : En partant du plus gros nombre possible,
# on cherche un nombre qui est à la fois et palindrome
# et décomposable en deux facteurs composés de trois chiffres.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    trouve = False
    i = 999 * 999

    while not trouve:
        if est_Palindrome(i):
            if decomposition_facteur_possible(i):
                trouve = True
            else:
                i -= 1
        else:
            i -= 1

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(i, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 906609 , en : 138.9231 ms.

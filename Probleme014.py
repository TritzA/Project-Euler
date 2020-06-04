import time
import math


def fin_temps(temps_fin, temps_debut):
    return (temps_fin - temps_debut) / math.pow(10, 6)


def longueur_collatz(nb):
    cmpt = 1
    while nb != 1:
        if nb % 2 == 0:
            nb = nb / 2
        else:
            nb = 3 * nb + 1
        cmpt += 1
    return cmpt


if __name__ == '__main__':
    n = 1
    i = 0
    while i < 10:
        print(n)
        if n % 3 == 0 or n % 3 == 1:
            n = 2 * n
        else:
            n = (2 * n - 1) / 3
        i += 1

# Résumé :
if __name__ == '__main__':
    temps_debut = time.time_ns()

    iterateur = 1000000
    taille_max = 0

    while iterateur > 1:
        taille_tempo = longueur_collatz(iterateur)
        # print(iterateur)
        if taille_max < taille_tempo:
            print(taille_max, "", iterateur)
            taille_max = taille_tempo
        #print(iterateur)
        if iterateur >= 500000:
            iterateur -= 1
        else:
            iterateur -= 2

    temps_fin = time.time_ns()
    reponse = taille_max
    print("Réponse :", reponse, ", en :", fin_temps(temps_fin, temps_debut), "ms.")
    # Réponse : 525 , en : 45880.7248 ms.

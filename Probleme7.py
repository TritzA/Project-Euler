import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


def est_premier(nb):
    nombre = 2
    premier = True

    while nombre < int(math.sqrt(nb))+1 and premier:
        if nb % nombre == 0:
            premier = False
        nombre += 1
    return premier


# Resume : On passe à travers les nombres en comptant à l'aide d'un compteur chaque fois qu'on en trouve un premier.
# La recherche se fait par bonds de deux à partir d'un nombre impair (3) et le compteur commence à 1 à cause du seul
# nombre premier pair (2).
if __name__ == '__main__':
    temps_initial = time.time_ns()
    compteur_premier = 1
    nombre_teste = 3

    while compteur_premier != 10001:
        if est_premier(nombre_teste):
            compteur_premier += 1
        nombre_teste += 2

    temps_fin = time.time()
    reponse = nombre_teste-2
    print("Reponse : ", reponse, ", en : ", fin_temps(temps_initial), "ms.")
    # Reponse :  104743 , en :  2279.6742 ms.

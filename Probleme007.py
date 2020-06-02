import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


def est_premier(nb):
    diviseur = 3
    premier = True
    max_diviseur = math.floor(math.sqrt(nb)) + 1
    while diviseur < max_diviseur and premier:
        if nb % diviseur == 0:
            premier = False
        diviseur += 2
    return premier


# Résumé : On passe à travers les nombres en comptant à l'aide d'un compteur chaque fois qu'on en trouve un premier.
# La recherche se fait par bonds de deux à partir d'un nombre impair (3) et le compteur commence à 1 à cause du seul
# nombre premier pair (2).
if __name__ == '__main__':
    temps_initial = time.time_ns()
    compteur_premier = 1
    nombre_teste = 3
    dernier_premier = 10001

    while compteur_premier != dernier_premier:
        if est_premier(nombre_teste):
            compteur_premier += 1
        nombre_teste += 2

    temps_fin = time.time()
    reponse = nombre_teste - 2
    print("Réponse :", reponse, ", en :", fin_temps(temps_initial), "ms.")
    # Réponse : 104743 , en : 346.8201 ms.

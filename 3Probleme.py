import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


def est_premier(nb):
    facteur = 3
    premier = True
    while facteur < int(math.sqrt(nb)) + 1 and premier:
        if nb % facteur == 0:
            premier = False
        else:
            facteur += 2
    return premier


# Resume : En partant de notre nombre de départ
# dès qu'on trouve une de ses facteurs premier,
# on le divise par celui-ci et on le garde en mémoire
# s'il est le plus grand trouvé. On recommence le
# même processus jusqu'à ce que le nombre restant
# soit premier ou qu'il soit plus petit que le plus
# grand facteur premier trouvé.
if __name__ == '__main__':
    temps_initial = time.time_ns()

    nombre = 600851475143
    recherche_facteur = 2
    facteur_max = 0
    trouve_facteur_premier = False

    if nombre % recherche_facteur == 0:
        trouve_facteur_premier = True
    else:
        recherche_facteur += 1

    while not est_premier(nombre):  # tant qu'on a pas réduit le nombre à un facteur premier

        while not trouve_facteur_premier or trouve_facteur_premier < facteur_max:

            if nombre % recherche_facteur == 0 and est_premier(recherche_facteur):
                trouve_facteur_premier = True
                if recherche_facteur < facteur_max:
                    facteur_max = recherche_facteur
            else:
                recherche_facteur += 2

        nombre = nombre / recherche_facteur  # on divise le nombre par un de ses facteurs premier
        trouve_facteur_premier = False

    temps_fin = time.time()
    reponse = int(nombre)
    print("Reponse :", reponse, ", en :", fin_temps(temps_initial), "ms.")
    # Reponse : 6857 , en : 0.9993 ms.
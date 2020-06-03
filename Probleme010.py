import time
import math


def fin_temps(temps_fin, temps_debut):
    return (temps_fin - temps_debut) / math.pow(10, 6)


def est_premier(nb):
    facteur = 3
    premier = True
    while facteur < int(math.sqrt(nb)) + 1 and premier:
        if nb % facteur == 0:
            premier = False
        else:
            facteur += 2
    return premier


# Résumé : On parcourt les nombres de 3 à 2M par bonds de 2 avec une somme commençant à 2 (seul nombre premier pair).
if __name__ == '__main__':
    temps_debut = time.time_ns()

    iterateur = 3
    somme = 2
    dernier_nombre = 2000000

    while iterateur < dernier_nombre:
        if est_premier(iterateur):
            somme += iterateur
        iterateur += 2

    temps_fin = time.time()
    reponse = somme
    print("Réponse :", reponse, ", en :", fin_temps(temps_fin, temps_debut), "ms.")
    # Réponse : 142913828922 , en : 67604.2771 ms.

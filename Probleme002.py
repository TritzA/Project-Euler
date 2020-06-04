import time
import math


def fin_temps(temps_fin, temps_debut):
    return (temps_fin - temps_debut) / math.pow(10, 6)


# Résumé : On parcourt la suite de Fibonacci par bonds de 3,
# chaque 3 nombres on trouve un nombre pair qu'on ajoute à la suite.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    nb_un = 1
    nb_deux = 1
    nb_trois = nb_un + nb_deux
    somme = 0
    fin = 4000000

    while nb_trois < fin:
        somme += nb_trois
        nb_un = nb_deux + nb_trois
        nb_deux = nb_un + nb_trois
        nb_trois = nb_un + nb_deux

    temps_fin = time.time_ns()
    reponse = somme
    print("Réponse :", reponse, ", en :", fin_temps(temps_fin, temps_debut), "ms.")
    # Réponse : 4613732 , en : 0 ms.

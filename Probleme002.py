import time
import math


def fin_temps(temps_fin, temps_debut):
    return (temps_fin - temps_debut) / math.pow(10, 6)


# Résumé : On parcourt la suite de Fibonacci par bonds de 3,
# chaque 3 nombres on trouve un nombre pair qu'on ajoute à la suite.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    nb_un = 0
    nb_deux = 1
    somme = 0
    dernier_nombre = 4000000

    while nb_un < dernier_nombre:
        nb_un = nb_un + nb_deux  # devient le troisième nombre
        nb_deux = nb_un + nb_deux  # devient le quatrième nombre (ce nombre est paire, si la suite commence à n=0,
        # si n%3 == 0, alors n est paire)
        nb_un = nb_un + nb_deux  # devient le cinquième
        nb_un, nb_deux = nb_deux, nb_un  # rétablie l'ordre pour que nb_un soit < que nb_deux
        somme += nb_un

    temps_fin = time.time_ns()
    reponse = somme - nb_un
    print("Réponse :", reponse, ", en :", fin_temps(temps_fin, temps_debut), "ms.")
    # Réponse : 4613732 , en : 0 ms.

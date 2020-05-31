import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


# Resume : On parcours la suite de Fibonacci dans
# une boucle allant jusqu'à 4M. Si on nouveau nombre
# de la suite est paire, on l'ajoute à la somme.
if __name__ == '__main__':
    temps_initial = time.time_ns()
    nb_un = 1
    nb_deux = 2
    somme = 2

    while nb_un < 4000000:
        tempo = nb_un
        nb_un = nb_deux
        nb_deux = nb_deux + tempo
        if nb_deux % 2 == 0:
            somme += nb_deux

    temps_fin = time.time()
    reponse = somme
    print("Reponse :", reponse, ", en :", fin_temps(temps_initial), "ms")
    # Reponse : 4613732 , en : 0.0 ms

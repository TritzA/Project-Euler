import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


# Resume : On effectue la somme des carrés puis le carré de la somme,
# puis on calcule la différence entre le deuxième et le premier.
if __name__ == '__main__':
    temps_initial = time.time_ns()

    somme_un = 0
    i = 1
    while i < 101:
        somme_un += i * i
        i += 1

    somme_deux = 0
    i = 1
    while i < 101:
        somme_deux += i
        i += 1
    somme_deux = somme_deux * somme_deux

    temps_fin = time.time()
    reponse = somme_deux - somme_un
    print("Reponse :", reponse, ", en :", fin_temps(temps_initial), "ms.")
    # Reponse : 25164150 , en : 0.0 ms.

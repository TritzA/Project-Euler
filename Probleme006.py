import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


def somme_carre():
    somme_carre = 0
    i = 1
    while i < 101:
        somme_carre += i * i
        i += 1
    return somme_carre


def carre_somme():
    carre_somme = 0
    i = 1
    while i < 101:
        carre_somme += i
        i += 1
    return carre_somme * carre_somme


# Résumé : On effectue la somme des carrés puis le carré de la somme,
# puis on calcule la différence entre le deuxième et le premier.
if __name__ == '__main__':
    temps_initial = time.time_ns()

    somme_carre = somme_carre()
    carre_somme = carre_somme()

    temps_fin = time.time()
    reponse = carre_somme - somme_carre
    print("Réponse :", reponse, ", en :", fin_temps(temps_initial), "ms.")
    # Réponse : 25164150 , en : 0.0 ms.

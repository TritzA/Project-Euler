import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


def est_multiple(nombre, multiple):
    return nombre % multiple == 0


# Resume : On parcours les nombres de 1 à 1000.
# Si un nombre multiple de 3 on l'ajoute à la somme.
# S'il ne l'est pas on verifie s'il est multiple de 5,
# si c'est le cas on l'ajoute à la somme.
if __name__ == '__main__':
    temps_initial = time.time_ns()
    nombre = 1
    somme = 0

    while nombre < 1000:
        if est_multiple(nombre, 3):
            somme += nombre
        elif est_multiple(nombre, 5):
            somme += nombre
        nombre += 1

    temps_fin = time.time()
    reponse = somme
    print("Reponse :", reponse ,", en :", fin_temps(temps_initial), "ms.")
    # Reponse : 233168 , en : 0.9993 ms.

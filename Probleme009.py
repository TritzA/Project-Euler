import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


def est_triplet_pytago(a, b, c):
    return math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)


# Résumé : Tente toutes les combinaisons de sommes possibles de
# trois nombres étant aussi des triplets pythagoriciens.
if __name__ == '__main__':
    temps_initial = time.time_ns()
    somme_max = 1000
    trouve = False
    a = 1
    b = 1
    c = 1

    while a < somme_max - b - c and not trouve:  # incrémentation de a

        c = somme_max - a - b
        while c > int((somme_max - a) / 2) and not trouve:  # variations de b et de c à la fois
            if est_triplet_pytago(a, b, c):
                produit = a * b * c
                trouve = True
            c -= 1
            b += 1
        b = 1
        a += 1

    temps_fin = time.time()
    reponse = produit
    print("Reponse :", reponse, ", en :", fin_temps(temps_initial), "ms.")
    # Reponse : 31875000 , en : 176.9186 ms.

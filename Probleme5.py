import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    return (temps_final - temps_initial) / math.pow(10, 6)


def est_divisible(nombre):
    return nombre % 5 == 0 and nombre % 7 == 0 and nombre % 9 == 0 and nombre % 11 == 0 \
           and nombre % 13 == 0 and nombre % 16 == 0 and nombre % 17 == 0 and nombre % 19 == 0
    # les premiers et les composés sans les premiers facteurs des composés


# Resume : Itérateur avance jusqu'à trouver un nombre divisible par les nombres de 1 a 20
# en testant chaque nombre une fois (exemple: on ne teste par 2 ni 3 car on test 16 et 9).
# L'itérateur avance par bond du produit des nombres premiers entre 2 et 20, car le nombre recherché
# doit forcément être une composition des ces nombres.
if __name__ == '__main__':
    temps_initial = time.time_ns()

    trouve = False
    bond = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19  # les nombre premiers
    iterateur = bond

    while not trouve:
        print(iterateur)
        if est_divisible(iterateur):
            trouve = True
        else:
            iterateur += bond

    temps_fin = time.time()
    reponse = iterateur
    print("Reponse : ", reponse, ", en : ", fin_temps(temps_initial), "ms.")
    # Reponse :  232792560 , en :  0.0 ms.

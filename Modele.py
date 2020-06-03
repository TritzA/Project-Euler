import time
import math


def fin_temps(temps_fin, temps_debut):
    return (temps_fin - temps_debut) / math.pow(10, 6)


# Résumé :
if __name__ == '__main__':
    temps_debut = time.time_ns()

    ### CODE ICI

    temps_fin = time.time_ns()
    reponse = -1
    print("Réponse :", reponse, ", en :", fin_temps(temps_fin, temps_debut), "ms.")
    # Réponse : -1 , en : -1 ms.

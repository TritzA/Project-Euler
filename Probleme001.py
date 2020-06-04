import time
import math


def fin_temps(temps_fin, temps_debut):
    return (temps_fin - temps_debut) / math.pow(10, 6)


def sommeMultiple(nb, fin=999):
    taille = math.floor(fin / nb) # nombre de multiples
    return int(taille * (((nb) + (nb * taille)) / 2)) # multiplie le nombre de multiples par sa valeur moyenne


# Résumé : Compte le nombre de multiple dans chaque ensemble,
# puis multiplie ce nombre par la valeur moyenne du multiple.
# Finalement, effectue l'union entre les ensembles et retire
# l'ensemble des multiples de 3 et de 5 (donc de 15) qui sont comptés deux fois.
if __name__ == '__main__':
    temps_debut = time.time_ns()
    fin = 999

    sommeTotale = sommeMultiple(3) + sommeMultiple(5) - sommeMultiple(15)

    temps_fin = time.time_ns()
    # l'ensemble des multiples des deux est compté deux fois
    reponse = sommeTotale
    print("Réponse :", reponse, ", en :", fin_temps(temps_fin, temps_debut), "ms.")
    # Réponse : 233168 , en : 0.0 ms.

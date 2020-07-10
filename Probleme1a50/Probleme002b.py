import math
import time

from Utilitaire import Gene


# Cette formule retourne le n ème terme de la suite de Fibonacci
def formule_binet(n):
    return round(phi ** n / sqrt_cinq)


# Retourne l'indice correspondant arrondi à la baisse d'un terme de la suite ou non
def inverse_formule_binet(t):
    return int(math.log(t * sqrt_cinq, phi))


# Résumé : Tant qu'on n'a pas dépassé la position du terme limite,
# on incrémente la somme de la valeur du n ème terme de la suite par bonds de 3.
if __name__ == '__main__':
    temps_debut = time.time()

    sqrt_cinq = math.sqrt(5)
    phi = (1 + sqrt_cinq) / 2  # valeur approximative de Phi

    somme = 0
    n = 0
    max = inverse_formule_binet(4000000)  # premier terme de la suite au dessus de 4M

    while n <= max:
        somme += formule_binet(n)
        n += 3  # chaque trois terme de la suite est pair

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 4613732 , en : 0.000 s.

import math
import time

import Uti


# Retourne le n ème terme de la suite de Fibonacci
def formule_binet(n):
    return round(phi ** n / sqrt_cinq)


# Retourne la primitive de la formule de binet
def primitive_formule_binet(n):
    return phi ** n / (sqrt_cinq * math.log(phi, math.e))


# Retourne l'indice correspondant arrondi à la baisse d'un terme de la suite ou non
def inverse_formule_binet(t):
    return int(math.log(t * sqrt_cinq, phi))


# Résumé : On tente de calculer la somme des termes pairs de la suite
# en multipliant leur nombre par leur valeur moyenne.
if __name__ == '__main__':
    temps_debut = time.time()

    sqrt_cinq = math.sqrt(5)
    phi = (1 + sqrt_cinq) / 2  # valeur approximative de Phi

    terme_fin = inverse_formule_binet(4000000)
    taille = terme_fin // 3

    valeur_moyenne = (primitive_formule_binet(terme_fin)) / (terme_fin - 3)

    somme = taille * valeur_moyenne

    temps_fin = time.time()
    Uti.rep(somme, temps_fin - temps_debut)
    # Réponse : 4613732 , en : 0.000 s.

import math
import time

from Utilitaire import Gene

# Résumé : On calcule le produit, puis on somme ces chiffres.
if __name__ == '__main__':
    temps_debut = time.time()

    somme = 0
    produit = str(math.factorial(99))
    for i in produit:
        somme += int(i)

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 648 , en : 0.000 s.

import time
import Utilitaire
import math

# Résumé : On calcule le produit, puis on somme ces chiffres.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    somme = 0
    produit = str(math.factorial(99))
    for i in produit:
        somme += int(i)

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(somme, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 648 , en : 0 ns.

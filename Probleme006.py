import time
import Utilitaire
import math

# Résumé : On effectue la somme des carrés puis le carré de la somme,
# puis on calcule la différence entre le deuxième et le premier.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    fin = 100
    somme_carre = fin * (fin + 1) * (2 * fin + 1) // 6
    carre_somme = int(math.pow(fin * (fin + 1) / 2, 2))

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(carre_somme - somme_carre, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 25164150 , en : 0 ns.

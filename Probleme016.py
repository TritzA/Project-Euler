import time
import Utilitaire

# Résumé : On effectue la puissance, puis on somme tous ces chiffres.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    somme = 0
    puissance = str(2 ** 1000)
    for i in puissance:
        somme += int(i)

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(somme, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 1366 , en : 0 ns.

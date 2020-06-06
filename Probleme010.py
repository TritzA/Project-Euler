import time
import Utilitaire

# Résumé : On parcourt les nombres de 3 à 2M par bonds de 2
# avec une somme commençant à 2 (seul nombre premier pair).
if __name__ == '__main__':
    temps_debut = time.time_ns()

    i = 3
    somme = 2
    dernier_nombre = 2000000
    while i < dernier_nombre:
        if Utilitaire.est_premier(i):
            somme += i
        i += 2

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(somme, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 142913828922 , en : 12996.8269 ms.

import time
import Utilitaire

# Résumé : On parcourt la suite de Fibonacci par bonds de 3,
# chaque 3 nombres on trouve un nombre pair qu'on ajoute à la suite.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    nb_un = 1
    nb_deux = 1
    nb_trois = nb_un + nb_deux
    somme = 0
    fin = 4000000

    while nb_trois < fin:
        somme += nb_trois
        nb_un = nb_deux + nb_trois
        nb_deux = nb_un + nb_trois
        nb_trois = nb_un + nb_deux

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(somme, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 4613732 , en : 0 ns.

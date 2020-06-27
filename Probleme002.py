import time
import Uti

# Résumé : On parcourt la suite de Fibonacci par bonds de 3,
# chaque 3 nombres on trouve un nombre pair qu'on ajoute à la suite.
if __name__ == '__main__':
    temps_debut = time.time()

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

    temps_fin = time.time()
    Uti.rep(somme, temps_fin - temps_debut)
    # Réponse : 4613732 , en : 0.000 s.

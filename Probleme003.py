import time
import Uti
import Nb

# Résumé : En partant de notre nombre de départ
# dès qu'on trouve un de ses facteurs premier,
# on le divise par celui-ci et on le garde en mémoire
# s'il est le plus grand trouvé. On recommence le
# même processus jusqu'à ce que le nombre restant
# soit premier ou qu'il soit plus petit que le plus
# grand facteur premier trouvé.
if __name__ == '__main__':
    temps_debut = time.time()

    nombre = 600851475143
    recherche_facteur = 2
    trouve_facteur_premier = False

    # test pour en cas de nombre pair,
    # permet de faire des bonds de 2 ensuite
    if nombre % recherche_facteur == 0:
        trouve_facteur_premier = True
    else:
        recherche_facteur += 1

    while not Nb.premier(nombre):  # tant qu'on a pas réduit le nombre à un facteur premier

        while not trouve_facteur_premier:

            if nombre % recherche_facteur == 0:
                trouve_facteur_premier = True
            else:
                recherche_facteur += 2

        # après avoir trouvé un facteur premier,
        # on divise le nombre par un de ses facteurs premier
        nombre = nombre // recherche_facteur
        trouve_facteur_premier = False

    temps_fin = time.time()
    Uti.rep(nombre, temps_fin - temps_debut)
    # Réponse : 6857 , en : 0.000 s.

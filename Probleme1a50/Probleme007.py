import time

from Utilitaire import Nb, Gene

# Résumé : On passe à travers les nombres en comptant à l'aide d'un compteur chaque fois qu'on en trouve un premier.
# La recherche se fait par bonds de deux à partir d'un nombre impair (3) et le compteur commence à 1 à cause du seul
# nombre premier pair (2).
if __name__ == '__main__':
    temps_debut = time.time()

    compteur_premier = 2
    nombre_teste = 3
    dernier_premier = 10001

    while compteur_premier != dernier_premier:
        nombre_teste += 2
        if Nb.premier(nombre_teste):
            compteur_premier += 1

    temps_fin = time.time()
    Gene.rep(nombre_teste, temps_fin - temps_debut)
    # Réponse : 104743 , en : 0.243 s.

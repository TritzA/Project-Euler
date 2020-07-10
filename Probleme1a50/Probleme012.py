import time

from Utilitaire import Gene

# Résumé : On passe de nombre triangulaire en nombre triangulaire
# en testant à chaque fois s'il ont plus de 500 diviseurs.
if __name__ == '__main__':
    temps_debut = time.time()

    objectif_diviseurs = 500
    nb_tri = 0
    nb_diviseurs = 0
    n = 0

    while nb_diviseurs < objectif_diviseurs:
        n += 1
        nb_tri += n
        nb_diviseurs = len(Gene.diviseurs(nb_tri))

    temps_fin = time.time()
    Gene.rep(nb_tri, temps_fin - temps_debut)
    # Réponse : 76576500 , en : 13.648 s.

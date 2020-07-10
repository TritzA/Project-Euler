import time

from Utilitaire import Gene

# Résumé : On traduit le problème par une suite qu'on somme de 1 à 1001.
# Pour ce faire on observe que les nombres 1, 3, 9 (du centre vers en haut à droite) sont carrés des impaires.
# C'est normal puisque la spirale est dans un carré (le début 1 de la spirale étant au milieu,
# celle-ci est donc forcément composée d'un nombre de lignes et de colonnes impairs).
# On peut facilement prouver qu'un nombre impair au carré est aussi impair,
# la suite sera donc en partie composée de carrés impairs. n étant l'ordre du carré,
# n = 0 forme un carré de (2n + 1) ^ 2 = 1, n = 1 de (2n + 1) ^ 2 = 9, n = 2 de (2n + 1) ^ 2 = 25.
# Suite à ce raisonnement, qui concerne la diagonale qui va en haut à droite, on peut constater que
# chaque terme de la diagonale de gauche est celui de la précédente moins 2n. On le constate, car chaque terme est
# dans l'autre coin du carré. Par exemple avec n = 1, si on a un côté de (2n + 1) = 3 on fera moins 2n pour aller
# à l'autre côté. Pour passer d'une complexité linéaire à constante, on détermine la somme Sn à partir de la suite
# trouvée (soit somme +=  4 * ((2 * n + 1) ** 2) - (n * 12) de 1 à ((max - 1) // 2 + 1) exclue en commençant à 1).
# Pour se faire, on développe et simplifie cette expression pour arriver à 16n ^ 2 + 4n+ 4. Ensuite, on calcule Sn
# à l'aide des propriétés des sommations et des formules de sommation de c, i et i ^ 2.
if __name__ == '__main__':
    temps_debut = time.time()

    n = (1001 - 1) // 2
    somme = (16 * (n * (2 * n + 1) * (n + 1) // 6)) + (4 * (n * (n + 1)) // 2) + (4 * n) + (1)

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 669171001 , en : 0.000 s.

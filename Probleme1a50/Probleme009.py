import time

from Utilitaire import Gene


def est_triplet_pytago(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


# Résumé : On tente toutes les combinaisons de sommes possibles de
# trois nombres étant aussi des triplets pythagoriciens.
if __name__ == '__main__':
    temps_debut = time.time()

    somme_max = 1000
    trouve = False

    # normalement on devrait commencer la variable a à la plus petite valeur de triplet 3,
    # mais on veut démarrer d'un nombre pair étant donné que a est incrémenter par 2 à chaque itération
    a = 4
    c = 1

    while not trouve:  # incrémentation de a

        b = 1
        c = somme_max - a - b
        while c > (somme_max - a) // 2 and not trouve:  # variations de b et de c à la fois
            if est_triplet_pytago(a, b, c):
                produit = a * b * c
                trouve = True
            c -= 1
            b += 1

        a += 2  # il y a forcément au moins un nombre pair dans un triplet

    temps_fin = time.time()
    Gene.rep(produit, temps_fin - temps_debut)
    # Réponse : 31875000 , en : 0.093 s.

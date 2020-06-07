import time
import Utilitaire


def est_triplet_pytago(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


# Résumé : Tente toutes les combinaisons de sommes possibles de
# trois nombres étant aussi des triplets pythagoriciens.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    somme_max = 1000
    trouve = False
    a = 1
    b = 1
    c = 1

    while a < somme_max - b - c and not trouve:  # incrémentation de a

        c = somme_max - a - b
        while c > int((somme_max - a) / 2) and not trouve:  # variations de b et de c à la fois
            if est_triplet_pytago(a, b, c):
                produit = a * b * c
                trouve = True
            c -= 1
            b += 1
        b = 1
        a += 1

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(produit, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 31875000 , en : 153.7837 ms.

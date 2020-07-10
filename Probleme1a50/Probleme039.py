import math
import time

from Utilitaire import Gene


def triplets(somme_max):
    liste = []
    for a in range(1, somme_max - 1):  # somme_max est exlue et on lui retire 1 car b et c valent minimalement 1
        for b in range(a, somme_max - 1):
            c = math.sqrt(a ** 2 + b ** 2)
            if c % 1 == 0:
                somme = a + b + int(c)
                liste.append(somme)
    return liste


# Résumé : On commence par mettre dans une liste la somme de tous les triplets pytahoricients
# sont la somme est plue petite ou égale à 1000. Ensuite, on parcours cette liste en comptant
# le nombre de fois ou est chaque nombre de 12 à 1000.
if __name__ == '__main__':
    temps_debut = time.time()

    liste = triplets(1000)

    max = 0
    min = 3 + 4 + 5  # somme du plus petit triplet
    for i in range(min, 1001, 2):
        tempo = 0
        for element in liste:
            if element == i:
                tempo += 1
        if tempo > max:
            max = tempo
            somme_max = i

    temps_fin = time.time()
    Gene.rep(somme_max, temps_fin - temps_debut)
    # Réponse : 840 , en : 0.926 s.

import math
import time

from Utilitaire import Nb, Gene

# Résumé : On parcours une boucle de nombre impair en nombre impair.
# S'ils sont composés, on tente de les écrire comme la somme d'un premier et du double d'un carré.
# Une fois que a est déterminé, on isole b dans la formule pour trouver sa valeur,
# ça évite un passage inutile dans une boucle. i = premiers[a] + 2 * b ^ 2 <=> b = math.sqrt((i - premiers[a]) / 2)
if __name__ == '__main__':
    temps_debut = time.time()

    trouve = False
    i = 7
    premiers = [2, 3, 5, 7]

    while not trouve:
        i += 2  # nombre forcément impair
        bon = False
        if Nb.compose(i):  # nombre composé

            a = 0
            while a < len(premiers) and not bon:  # teste les valeurs de a qui sont premiers
                b = math.sqrt((i - premiers[a]) / 2)  # isole b
                if b % 1 == 0 and i == premiers[a] + 2 * (b ** 2):  # si b est un entier et que l'égalité est vrai
                    bon = True
                a += 1

        else:
            bon = True  # si le nombre n'est pas composé, la conjecture n'est pas invalidée
        if not bon:
            trouve = True

        if Nb.premier(i):
            premiers.append(i)  # on conserve les nombres premiers quand on les trouve

    temps_fin = time.time()
    Gene.rep(i, temps_fin - temps_debut)
    # Réponse : 5777 , en : 0.130 s.

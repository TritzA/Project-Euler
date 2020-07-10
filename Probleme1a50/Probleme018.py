import time

from Utilitaire import Gene

taille = 15


def lire_mat():
    nombre = Gene.lire("Probleme067")
    mat = "mat = ["
    i = 0
    while i < taille:
        if i != 0:
            mat += ",["
        else:
            mat += "["
        j = 0
        while j <= i:
            pos = (i * (i + 1)) // 2 * 3 + j * 3
            if j != i:
                mat += str(int(nombre[pos:pos + 2])) + ", "
            else:
                mat += str(int(nombre[pos:pos + 2]))
            j += 1
        mat += "]"
        i += 1
    mat += "]"
    print(mat)

# Résumé : En partant de la dernière ligne, on compare les deux points possibles d'arrivée sur celle-ci
# en partant de l'avant-dernière ligne. On ajoute ensuite à la dernière ligne la plus grande des deux valeurs possibles.
# On répète ce processus sur l'entièreté des colonnes de chaque ligne. À la fin, la matrice est complètement transformée
# et nombre au sommet de la pyramide indique la plus grande somme possible.
if __name__ == '__main__':
    temps_debut = time.time()

    # lire_mat()
    mat = [[75],
           [95, 64],
           [17, 47, 82],
           [18, 35, 87, 10],
           [20, 4, 82, 47, 65],
           [19, 1, 23, 75, 3, 34],
           [88, 2, 77, 73, 7, 63, 67],
           [99, 65, 4, 28, 6, 16, 70, 92],
           [41, 41, 26, 56, 83, 40, 80, 70, 33],
           [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
           [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
           [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
           [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
           [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
           [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

    ligne = taille - 1
    while ligne > 0:
        colonne = 0
        while colonne < ligne:
            if mat[ligne][colonne] > mat[ligne][colonne + 1]:  # si le nombre de gauche est le plus grand
                mat[ligne - 1][colonne] += mat[ligne][colonne]
            else:  # si le nombre de droite est le plus grand
                mat[ligne - 1][colonne] += mat[ligne][colonne + 1]
            colonne += 1
        ligne -= 1

    temps_fin = time.time()
    Gene.rep(mat[0][0], temps_fin - temps_debut)
    # Réponse : 1074 , en : 0.000 s.

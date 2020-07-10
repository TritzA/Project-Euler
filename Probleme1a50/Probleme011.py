import time

from Utilitaire import Gene


def horizontale(mat):
    produit_max = 0
    i = 0
    while i < 20:
        j = 0
        while j < 20 - 3:
            produit = mat[i][j] * mat[i][j + 1] * mat[i][j + 2] * mat[i][j + 3]
            if produit == 0 and j > 2:
                j += 5
            elif produit_max < produit:
                produit_max = produit
            j += 1
        i += 1
    return produit_max


def verticale(mat):
    produit_max = 0
    j = 0
    while j < 20:
        i = 0
        while i < 20 - 3:
            produit = mat[i][j] * mat[i + 1][j] * mat[i + 2][j] * mat[i + 3][j]
            if produit == 0 and i > 2:
                i += 5
            elif produit_max < produit:
                produit_max = produit
            i += 1
        j += 1
    return produit_max


def diagonale_un(mat):
    produit_max = 0
    i = 0
    while i < 20 - 3:
        j = 0
        while j < 20 - 3:
            produit = mat[i][j] * mat[i + 1][j + 1] * mat[i + 2][j + 2] * mat[i + 3][j + 3]
            if produit_max < produit:
                produit_max = produit
            j += 1
        i += 1
    return produit_max


def diagonale_deux(mat):
    produit_max = 0
    i = 0
    while i < 20 - 3:
        j = 3
        while j < 20:
            produit = mat[i][j] * mat[i + 1][j - 1] * mat[i + 2][j - 2] * mat[i + 3][j - 3]
            if produit_max < produit:
                produit_max = produit
            j += 1
        i += 1
    return produit_max


def lire_matrice():
    chaine = Gene.lire("Probleme011")
    i = 0
    mat = "mat = ["
    while i < 20 * 20 * 3:
        if (i // 3) % 20 == 0:
            mat += "[" + str(int(chaine[i:i + 2]))
        elif (i // 3) % 20 == 19 and (i // 3) // 20 == 19:
            mat += "," + str(int(chaine[i:i + 2])) + "]]"
        elif (i // 3) % 20 == 19:
            mat += "," + str(int(chaine[i:i + 2])) + "],"
        else:
            mat += "," + str(int(chaine[i:i + 2]))
        i += 3
    print(mat)


# Résumé : On trouve le produit de chacune quatre dispositions possibles.
# Ensuite, on sélectionne le produit maximum des quatre.
# À noter que lorsqu'on arrive sur un 0 dans la recherche horizontale ou verticale,
# on saute le calcul des produits suivant qui auraient été égaux à 0.
if __name__ == '__main__':
    temps_debut = time.time()

    # lire_matrice()
    mat = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
           [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
           [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
           [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
           [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
           [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
           [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
           [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
           [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
           [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
           [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
           [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
           [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
           [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
           [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
           [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
           [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
           [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
           [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
           [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
    array = [horizontale(mat), verticale(mat), diagonale_un(mat), diagonale_deux(mat)]

    temps_fin = time.time()
    Gene.rep(max(array), temps_fin - temps_debut)
    # Réponse : 70600674 , en : 0.000 s.

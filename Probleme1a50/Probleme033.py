import time

from Utilitaire import Nb, Gene


def propriete(a, b):  # déterminer si la fraction respecte la propriété
    if int(a) % 10 == int(b) % 10 == 0:
        return False
    if a[0] == b[0] and int(b[1]) != 0:
        if int(a[1]) / int(b[1]) == int(a) / int(b):
            return True
    elif a[0] == b[1] and int(b[0]) != 0:
        if int(a[1]) / int(b[0]) == int(a) / int(b):
            return True
    elif a[1] == b[0] and int(b[1]) != 0:
        if int(a[0]) / int(b[1]) == int(a) / int(b):
            return True
    elif a[1] == b[1] and int(b[0]) != 0:
        if int(a[0]) / int(b[0]) == int(a) / int(b):
            return True
    else:
        return False


def reduire(a, b, premiers):  # réduire une fraction en fraction irréductible à l'aide d'une liste de premiers
    i = 0
    valeur = premiers[i]
    while valeur <= a and valeur <= b:
        if a % valeur == 0 and b % valeur == 0:
            a //= valeur
            b //= valeur
        else:
            i += 1
            valeur = premiers[i]
    return a, b


# Résumé : On parcourt tous les couples possibles en testant s'ils respectent la propriété.
# Si c'est le cas, on multiplie cette fraction au produit principal. On finit par
# réduire le produit principal et obtenir la valeur de son dénominateur.
if __name__ == '__main__':
    temps_debut = time.time()

    premiers = [2]
    for i in range(3, 100, 2):
        if Nb.premier(i):
            premiers.append(i)

    max = 0
    produit_a = 1
    produit_b = 1
    for i in range(10, 100 // 2):  # le nombre doit être composé de deux chiffres
        for j in range(100 // 2, 100):  # on évite de tester deux fois le même couple
            if propriete(str(i), str(j)):
                tempo = reduire(i, j, premiers)
                produit_a *= tempo[0]
                produit_b *= tempo[1]

    produit_final = tempo = reduire(produit_a, produit_b, premiers)
    temps_fin = time.time()
    Gene.rep(produit_final[1], temps_fin - temps_debut)
    # Réponse : 100 , en : 0.000 s.

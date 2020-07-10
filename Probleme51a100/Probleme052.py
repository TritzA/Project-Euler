import time

from Utilitaire import Gene


def meme_chiffre(a, b):
    a = str(a)
    chiffre_a = set()
    for chiffre in a:
        chiffre_a.add(chiffre)

    b = str(b)
    chiffre_b = set()
    for chiffre in b:
        chiffre_b.add(chiffre)

    if chiffre_a == chiffre_b:
        return True

    return False


def propriete(n):
    for i in range(2, 7):
        if not meme_chiffre(n, n * i):
            return False
    return True


# Résumé : On parcourt les entiers positifs jusqu'à trouver un nombre qui vérifie la propriété.
# Pour tester si deux nombres sont formés des mêmes chiffres,
# on place les chiffres des nombres dans des ensemble, puis on teste l'égalité entre ces deux ensembles.
if __name__ == '__main__':
    temps_debut = time.time()

    trouve = False
    i = 0
    while not trouve:
        i += 1
        if propriete(i):
            trouve = True

    temps_fin = time.time()
    Gene.rep(i, temps_fin - temps_debut)
    # Réponse : 142857 , en : 0.778 s.

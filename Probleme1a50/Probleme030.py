import time

from Utilitaire import Gene


def somme_puissances(n):
    somme = 0
    n = str(n)
    for i in n:
        somme += int(i) ** 5
    return somme


# Résumé : On calcule la somme des puissances de chiffres composant les nombres de 2 à la limite maximale.
# Si cette somme est égale au nombre, on l'incrémente à la somme principale.
if __name__ == '__main__':
    temps_debut = time.time()

    max = 6 * 9 ** 5
    min = 2
    somme = 0
    for i in range(2, max):
        if i == somme_puissances(i):
            somme += i

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 443839 , en : 2.331 s.

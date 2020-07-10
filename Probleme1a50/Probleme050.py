import time

from Utilitaire import Nb, Gene


def lister_premiers(max):
    liste = [2]
    for i in range(3, max, 2):
        if Nb.premier(i):
            liste.append(i)
    return liste


# Résumé :
if __name__ == '__main__':
    temps_debut = time.time()

    premiers = lister_premiers(1000000)
    print(premiers)

    taille = 0
    max = 0
    taille_max = 6

    for debut in range(0, len(premiers) - taille):
        somme = 0

        for taille in range(taille_max, len(premiers)):
            print(taille, taille_max)
            for i in range(debut, debut + taille):
                somme += premiers[i]

            if max < somme:
                somme = max
                taille_max = taille

    temps_fin = time.time()
    Gene.rep(-1, temps_fin - temps_debut)
    # Réponse : -1 , en : -1 s.

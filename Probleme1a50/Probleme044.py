import time

from Utilitaire import Nb, Gene


def penta(n):
    return int(n * (3 * n - 1) / 2)


# Résumé : Dans une liste, on ajoute les nombres pentagonaux par incrément.
# À chaque ajout, on teste si cette valeur peut se combiner avec un autre
# nombre de la liste pour que leur somme et leur différence soient un nombre pentagonale.
if __name__ == '__main__':
    temps_debut = time.time()

    n = 1
    nb_penta = list()
    nb_penta.append(penta(n))
    n += 1
    nb_penta.append(penta(n))
    n += 1

    trouve = False
    while not trouve:

        tempo = penta(n)
        n += 1
        for i in nb_penta:
            if Nb.pentagonal(tempo - i) and Nb.pentagonal(tempo + i):
                d = tempo - i
                trouve = True

        nb_penta.append(tempo)

    temps_fin = time.time()
    Gene.rep(d, temps_fin - temps_debut)
    # Réponse : 5482660 , en : 4.044 s.

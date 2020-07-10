import time

from Utilitaire import Nb, Gene


def propriete(n):
    deux = str(n) + str(2 * n)
    if Nb.pandigital(deux):
        return deux

    trois = str(n) + str(2 * n) + str(3 * n)
    if Nb.pandigital(trois):
        return trois

    return ""


# Résumé : On parcourt les nombres en tentant de les décomposer en palindromes.
if __name__ == '__main__':
    temps_debut = time.time()

    pandigitals = set()
    trouve = False

    for i in range(1, 10000):
        pan_tempo = propriete(i)
        if pan_tempo != "":
            pandigitals.add(pan_tempo)

    max = max(pandigitals)

    temps_fin = time.time()
    Gene.rep(max, temps_fin - temps_debut)
    # Réponse : 932718654 , en : 0.033 s.

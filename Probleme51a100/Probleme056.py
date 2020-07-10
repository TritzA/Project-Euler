import time

from Utilitaire import Gene


def somme_chiffres(n):
    n = str(n)
    somme = 0
    for chiffre in n:
        somme += int(chiffre)
    return somme


# Résumé : On fait varier a et b entre 90 et 99 en conservant la
# plus grande somme des chiffres trouvés à chaque fois.
# Notons que 90^90 possède 22 chiffres de plus que 99^99.
if __name__ == '__main__':
    temps_debut = time.time()

    max = 0
    for a in range(90, 100):
        for b in range(90, 100):
            puissance = somme_chiffres(a ** b)
            if max < puissance:
                max = puissance

    temps_fin = time.time()
    Gene.rep(max, temps_fin - temps_debut)
    # Réponse : 972 , en : 0.000 s.

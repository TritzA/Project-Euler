import time

from Utilitaire import Gene


def nb_fac_premier(n):
    premiers = set()
    recherche = 2
    while recherche * recherche <= n:
        while (n % recherche) == 0:
            n //= recherche
            if not recherche in premiers:
                premiers.add(recherche)

        recherche += 1
    if n > 1 and not n in premiers:
        premiers.add(n)
    return premiers


# Résumé : On parcourt les nombres entier jusqu'a trouver une séance de 4 nombres qui respecte la propriété.
if __name__ == '__main__':
    temps_debut = time.time()

    taille = 4

    trouve = False
    i = 1
    while not trouve:
        i += 1
        sequence = 0
        bon = True
        while bon and sequence < taille:
            if len(nb_fac_premier(i + sequence)) != taille:
                bon = False
            sequence += 1
        if bon:
            trouve = True

    temps_fin = time.time()
    Gene.rep(i, temps_fin - temps_debut)
    # Réponse : 134043 , en : 3.331 s.

import time

from Utilitaire import Gene


def longueur_cycle(nb):
    reste = 10
    i = 0
    # Calcule les décimales tant que le reste n'est pas égal à 10
    while reste != 10 or i < 1:
        reste = (reste % nb) * 10
        i += 1
    return i


# Résumé : Résolution très mathématique, la page Wikipédia "Développement décimal périodique" aide beaucoup.
# On calcule chaque cycle en ajoutant des dizaines au reste jusqu'à retomber sur un reste de 0
if __name__ == '__main__':
    temps_debut = time.time()

    max = 0
    for i in range(3, 1000, 2):
        if i % 5 != 0:
            taille = longueur_cycle(i)
            if max < taille:
                max = taille
                max_nb_cycle = i

    temps_fin = time.time()
    Gene.rep(max_nb_cycle, temps_fin - temps_debut)
    # Réponse : 983 , en : 0.012 s.

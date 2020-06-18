import time
import Utilitaire


def est_bissexile(annee):
    if annee % 400 == 0:
        bissextile = True
    elif annee % 100 == 0:
        bissextile = False
    elif annee % 4 == 0:
        bissextile = True
    else:
        bissextile = False
    return bissextile


def nombre(debut, bissex):
    nb = 0
    mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]
    i = 0

    while i < 12:
        if debut == 0:
            nb += 1

        if i == 1 and bissex:
            debut += mois[12]
        else:
            debut += mois[i]
        debut %= 7
        i += 1
    return nb, debut


# Résumé : On teste si tous les premier du mois du XXe sciècle était un dimanche
# par bonds du nombre de jours dans un mois.
# Les jours de la semaines sont numérotés de 0 (dimanche) à 6 (samedi).
if __name__ == '__main__':
    temps_debut = time.time_ns()

    nb = 0
    jour = 2  # le premier janvier 1901 était un mardi
    for annee in range(1901, 2001):
        bissex = est_bissexile(annee)
        ajout, jour = nombre(jour, bissex)
        nb += ajout

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(nb, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 171 , en : 0 ns.

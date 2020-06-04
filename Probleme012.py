import time
import math


def fin_temps(temps_fin, temps_debut):
    return (temps_fin - temps_debut) / math.pow(10, 6)


def nb_tri_debut(n):
    return n*(n+1)/2


def nouveau_diviseurs(nb):
    i = 1
    cmpt_diviseurs = 0
    while i <= nb:
        if nb % i == 0:
            cmpt_diviseurs += 1
        i += 1
    return cmpt_diviseurs


# Résumé :
if __name__ == '__main__':
    temps_debut = time.time_ns()

    objectif_diviseurs = 5
    indice_plus_petit_tri_possible = 1
    nb_tri = nb_tri_debut(indice_plus_petit_tri_possible)
    nb_diviseurs = 0
    iterateur = 2

    while nb_diviseurs <= objectif_diviseurs:
        nb_tri += iterateur
        iterateur += 1
        if nb_diviseurs < nouveau_diviseurs(nb_tri):
            nb_diviseurs = nouveau_diviseurs(nb_tri)
            print("nouveau diviseur", nb_diviseurs)
        print(nb_tri, "nb tri")
        #time.sleep(1)

    temps_fin = time.time_ns()
    reponse = nb_tri
    print("Réponse :", reponse, ", en :", fin_temps(temps_fin, temps_debut), "ms.")
    # Réponse : -1 , en : -1 ms.

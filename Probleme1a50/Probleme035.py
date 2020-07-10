import time

from Utilitaire import Nb, Gene


def lister_premiers(max):
    liste = ["2"]
    for i in range(3, max, 2):
        if Nb.premier(i) and pas_pair(str(i)):
            liste.append(str(i))
    return liste


def rotation(ancien):
    nombres = []
    for taille in range(0, len(ancien)):
        nouveau = ""
        for i in range(1, len(ancien)):
            nouveau += ancien[i]
        nouveau += ancien[0]
        nombres.append(int(nouveau))
        ancien = nouveau
    return nombres


def pas_pair(chaine):
    if "0" in chaine:
        return False
    elif "2" in chaine:
        return False
    elif "4" in chaine:
        return False
    elif "6" in chaine:
        return False
    elif "8" in chaine:
        return False
    return True


# Résumé : On teste si chacun des nombres premiers d'une liste est premier circulaire.
# Dans cette liste, il n'y a que des premiers composés de chiffres impairs.
if __name__ == '__main__':
    temps_debut = time.time()

    premiers = lister_premiers(1000000)

    cmpt = 0
    element = 0
    while element < len(premiers):  # On teste chaque premier

        cercle = rotation(premiers[element])  # cercle contient toutes les rotations possibles
        premier_circulaire = True

        nombre = 0
        while nombre < len(cercle) and premier_circulaire:
            derive = cercle[nombre]

            if not Nb.premier(derive):
                premier_circulaire = False  # Dès qu'on trouve un nombre de cercle non premier on sort de la boucle
            elif derive in premiers:
                premiers.remove(derive)  # On enlève chaque premier circulaire trouvé de la liste
            nombre += 1

        if premier_circulaire:  # Si à cette étape premier_circulaire est toujours vrai, le test est positif
            cmpt += 1

        element += 1

    temps_fin = time.time()
    Gene.rep(cmpt, temps_fin - temps_debut)
    # Réponse : 55 , en : 8.188 s.

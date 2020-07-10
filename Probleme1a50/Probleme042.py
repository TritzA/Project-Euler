import time

from Utilitaire import Nb, Gene


def nombre_mot(mot):
    somme = 0
    for i in range(0, len(mot)):
        somme += correspondance(mot[i])
    return somme


def correspondance(char):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(char) + 1


# Résumé : On parcourt tous les mots, s'ils sont triangulaires, on ajoute 1 au compteur.
if __name__ == '__main__':
    temps_debut = time.time()

    contenu = Gene.lire("Probleme042")
    contenu = contenu[1:] + ",\"*\","
    cmpt = 0

    virgule = contenu.index(',')
    mot = contenu[: virgule - 1]
    while mot[0] != "*":

        if Nb.triangulaire(nombre_mot(mot)):
            cmpt += 1
        contenu = contenu[virgule + 2:]

        virgule = contenu.index(',')
        mot = contenu[: virgule - 1]

    temps_fin = time.time()
    Gene.rep(cmpt, temps_fin - temps_debut)
    # Réponse : 162 , en : 0.006 s.

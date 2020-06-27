import time
import Uti


def lister():
    contenu = Uti.lire("Probleme022.txt")
    contenu = contenu[1:] + ",\"*\","

    virgule = contenu.index(',')
    mot = contenu[: virgule - 1]
    noms = []
    while mot[0] != "*":
        noms.append(mot)
        contenu = contenu[virgule + 2:]
        virgule = contenu.index(',')
        mot = contenu[: virgule - 1]
    return noms


def compter(mot):
    somme = 0

    for char in mot:
        somme += correspondance(char)

    return somme


def correspondance(char):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(char) + 1


# Résumé : On place tous les noms dans une liste.
# Ensuite, on trie cette liste par ordre alphabétique.
# Puis, on calcule le nombre de chaque mot qu'on multiplie par sa position.
# La somme est incrémentée de cette valeur jusqu'à la fin du parcours de la liste.
if __name__ == '__main__':
    temps_debut = time.time()

    noms = lister()

    noms.sort()

    somme = 0
    for i in range(0, len(noms)):
        somme += compter(noms[i]) * (i + 1)

    temps_fin = time.time()
    Uti.rep(somme, temps_fin - temps_debut)
    # Réponse : 871198282 , en : 0.078 s.

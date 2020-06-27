import time
import Uti


def unites():
    somme = len("one")
    somme += len("two")
    somme += len("three")
    somme += len("four")
    somme += len("five")
    somme += len("six")
    somme += len("seven")
    somme += len("eight")
    somme += len("nine")
    return somme * 190


def dix_a_dix_neuf():
    somme = len("ten")
    somme += len("eleven")
    somme += len("twelve")
    somme += len("thirteen")
    somme += len("fourteen")
    somme += len("fifteen")
    somme += len("sixteen")
    somme += len("seventeen")
    somme += len("eighteen")
    somme += len("nineteen")
    return somme * 10


def dizaines():
    somme = len("twenty")
    somme += len("thirty")
    somme += len("forty")
    somme += len("fifty")
    somme += len("sixty")
    somme += len("seventy")
    somme += len("eighty")
    somme += len("ninety")
    return somme * 100


def cent():
    return len("hundred") * 900


def et():
    return len("and") * 891


def mille():
    return len("one") + len("thousand")


# Résumé : On calcule la somme des lettres en multipliant la taille des mots par leur nombre d'apparitions.
if __name__ == '__main__':
    temps_debut = time.time()

    somme = unites() + dix_a_dix_neuf() + dizaines() + cent() + et() + mille()

    temps_fin = time.time()
    Uti.rep(somme, temps_fin - temps_debut)
    # Réponse : 21124 , en : 0.000 s.

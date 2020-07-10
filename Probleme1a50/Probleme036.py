import time

from Utilitaire import Nb, Gene

# Résumé : On teste à chaque fois qui le nombre est un palindrome en base 10.
# Si c'est le cas, on teste s'il l'est en binaire.
# Si c'est aussi le cas, on incrémente le nombre à la somme.
if __name__ == '__main__':
    temps_debut = time.time()

    somme = 0
    for i in range(0, 1000000):
        if Nb.palindrome(i):
            if Nb.palindrome(str(bin(i))[2:]):
                somme += i

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 872187 , en : 1.643 s.

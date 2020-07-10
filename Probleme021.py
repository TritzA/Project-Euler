import time

import Nb
import Uti

# Résumé : On passe à travers les nombres de 2 à 10000
# exclu en charchant si chaque nombre à un nombre ami.
if __name__ == '__main__':
    temps_debut = time.time()

    somme = 0
    a = 2
    while a < 10000:
        if Nb.amical(a):
            somme += a
        a += 1

    temps_fin = time.time()
    Uti.rep(somme, temps_fin - temps_debut)
    # Réponse : 31626 , en : 0.244 s.

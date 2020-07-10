import time

import Uti

# Résumé : On parcourt la suite de Fibonacci par bonds de 3,
# chaque 3 nombres on trouve un nombre pair qu'on ajoute à la suite.
if __name__ == '__main__':
    temps_debut = time.time()

    a = 1
    b = 1
    c = a + b
    somme = 0
    fin = 4000000

    while c < fin:
        somme += c
        a = b + c
        b = a + c
        c = a + b

    temps_fin = time.time()
    Uti.rep(somme, temps_fin - temps_debut)
    # Réponse : 4613732 , en : 0.000 s.

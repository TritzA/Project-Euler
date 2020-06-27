import time
import Uti

# Résumé : On parcourt la suite de Fibonacci jusqu'à trouver un nombre formé de 1000 chiffres.
if __name__ == '__main__':
    temps_debut = time.time()

    a = 0
    b = 1
    cmpt = 0
    while len(str(a)) != 1000:
        a, b = b, a + b
        cmpt += 1

    temps_fin = time.time()
    Uti.rep(cmpt, temps_fin - temps_debut)
    # Réponse : 4782 , en : 0.171 s.

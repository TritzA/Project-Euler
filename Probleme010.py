import time
import Uti
import Nb

# Résumé : On parcourt les nombres de 3 à 2M par bonds de 2
# avec une somme commençant à 2 (seul nombre premier pair).
if __name__ == '__main__':
    temps_debut = time.time()

    i = 3
    somme = 2
    dernier_nombre = 2000000
    while i < dernier_nombre:
        if Nb.premier(i):
            somme += i
        i += 2

    temps_fin = time.time()
    Uti.rep(somme, temps_fin - temps_debut)
    # Réponse : 142913828922 , en : 14.74 s.

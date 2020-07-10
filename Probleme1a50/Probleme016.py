import time

from Utilitaire import Gene

# Résumé : On effectue la puissance, puis on somme tous ces chiffres.
if __name__ == '__main__':
    temps_debut = time.time()

    somme = 0
    puissance = str(2 ** 1000)
    for i in puissance:
        somme += int(i)

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 1366 , en : 0.000 s.

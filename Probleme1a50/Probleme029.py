import time

from Utilitaire import Gene

# Résumé : On parcourt les deux boucles en ajoutant les nouvelles puissances dans l'ensemble.
# Ensuit, on évalue la cadinalité de cet ensemble
if __name__ == '__main__':
    temps_debut = time.time()

    combinaisons = set()
    for a in range(2, 101):
        for b in range(2, 101):
            combinaisons.add(a ** b)

    temps_fin = time.time()
    Gene.rep(len(combinaisons), temps_fin - temps_debut)
    # Réponse : 9183 , en : 0.000 s.

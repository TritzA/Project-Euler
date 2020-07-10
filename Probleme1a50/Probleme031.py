import time

from Utilitaire import Gene

# Résumé : On force la solution en testant toutes les possibilités.
# Notons qu'il n'y a pas de boucle pour le 1, on l'isole dans l'équation
# pour trouver sa valeur. J'aurais aimé trouver un algorithme plus optimisé
# (sûrement récursif) pour ce problème. Je m'y remettrai quand je pourrai.
if __name__ == '__main__':
    temps_debut = time.time()

    cmp = 0
    total = 200
    for a in range(0, total + 1, 200):
        total = 200 - a
        for b in range(0, total + 1, 100):
            total = 200 - a - b
            for c in range(0, total + 1, 50):
                total = 200 - a - b - c
                for d in range(0, total + 1, 20):
                    total = 200 - a - b - c - d
                    for e in range(0, total + 1, 10):
                        total = 200 - a - b - c - d - e
                        for f in range(0, total + 1, 5):
                            total = 200 - a - b - c - d - e - f
                            for g in range(0, total + 1, 2):
                                h = 200 - a - b - c - d - e - f - g
                                if h >= 0:
                                    cmp += 1

    temps_fin = time.time()
    Gene.rep(cmp, temps_fin - temps_debut)
    # Réponse : 73682 , en : 0.067 s.

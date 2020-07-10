import time

from Utilitaire import Gene

# Résumé : On parcourt toutes les valeurs possibles en testant si la combinaison dépasse le million.
if __name__ == '__main__':
    temps_debut = time.time()

    cmpt = 0
    for n in range(23, 101):  # 23 est le premier n permettant de dépasser le million
        for r in range(4, n):  # 4 est le premier r permettant de dépasser le million
            if Gene.combinaison(n, r) > 1000000:
                cmpt += 1

    temps_fin = time.time()
    Gene.rep(cmpt, temps_fin - temps_debut)
    # Réponse : 4075 , en : 0.023 s.

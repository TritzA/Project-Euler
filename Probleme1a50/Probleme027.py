import time

from Utilitaire import Nb, Gene


def fonction(a, b, n):
    return n ** 2 + a * n + b


# Résumé : On passe dans deux boucles en faisant varier a et b.
# Notons que le premier entier trouvé doit être premier losque le compteur est à 0.
# Quand n = 0 la fonction vaut 0 ^ 2 + a * 0 + b donc b. b ne peut donc pas être négatif.
if __name__ == '__main__':
    temps_debut = time.time()

    max = 0
    produit = 0
    for a in range(-1000, 1000):
        for b in range(3, 1001, 2):  # min b = 3 parce que le permier nombre premier doit être impair

            cmpt = 1  # le premier entier 2 est déjà trouvé
            suite_premier = True

            while suite_premier:
                if Nb.premier(fonction(a, b, cmpt)):
                    cmpt += 1
                else:
                    if max < cmpt:
                        max = cmpt
                        produit = a * b
                    suite_premier = False

    temps_fin = time.time()
    Gene.rep(produit, temps_fin - temps_debut)
    # Réponse : -59231 , en : 3.139 s.

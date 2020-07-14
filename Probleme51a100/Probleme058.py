import time

from Utilitaire import Gene
from Utilitaire import Nb

# Résumé : D'abord, on trouve la valeur des nouveaux nombres grâce à leur position relative
# à la diagonale inférieure droite. Ensuite, s'ils sont premiers, on les ajoute au compteur de nombres premiers.
# Après chaque itération, on calcule si le taux est sous 10%.
if __name__ == '__main__':
    temps_debut = time.time()

    taux = 1
    taille_cote = 1
    tot = 1  # compteur de nombres sur les diagonales
    prem = 0  # compteur de nombres premiers sur les diagonales
    while taux > 0.1:
        taille_cote += 2
        tot += 4
        inf_droit = taille_cote ** 2

        bond = taille_cote - 1
        for no in range(1, 4): # test des nombres aux trois autres coins
            if Nb.premier(inf_droit - (no * bond)):
                prem += 1

        taux = prem / tot  # calcul du taux afin de savoir si on est sous les 10%

    temps_fin = time.time()
    Gene.rep(taille_cote, temps_fin - temps_debut)
    # Réponse : 26241 , en : 9.326 s.

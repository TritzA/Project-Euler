import time
import Uti


def sommeMultiple(nb, fin=999):
    taille = fin // nb  # nombre de multiples
    return taille * (((nb) + (nb * taille)) / 2)  # multiplie le nombre de multiples par sa valeur moyenne


# Résumé : Compte le nombre de multiple dans chaque ensemble,
# puis multiplie ce nombre par la valeur moyenne du multiple.
# Finalement, effectue l'union entre les ensembles et retire
# l'ensemble des multiples de 3 et de 5 (donc de 15) qui sont comptés deux fois.
if __name__ == '__main__':
    temps_debut = time.time()

    # l'ensemble des multiples de 3 et de 5 est compté deux fois
    union = 3 * 5
    sommeTotale = int(sommeMultiple(3) + sommeMultiple(5) - sommeMultiple(union))

    temps_fin = time.time()
    Uti.rep(sommeTotale, temps_fin - temps_debut)
    # Réponse : 233168 , en : 0.000 s

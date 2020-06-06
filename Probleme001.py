import time
import Utilitaire


def sommeMultiple(nb, fin=999):
    taille = fin // nb  # nombre de multiples
    return taille * (((nb) + (nb * taille)) / 2)  # multiplie le nombre de multiples par sa valeur moyenne


# Résumé : Compte le nombre de multiple dans chaque ensemble,
# puis multiplie ce nombre par la valeur moyenne du multiple.
# Finalement, effectue l'union entre les ensembles et retire
# l'ensemble des multiples de 3 et de 5 (donc de 15) qui sont comptés deux fois.
if __name__ == '__main__':
    temps_debut = time.time_ns()
    fin = 999

    # l'ensemble des multiples des deux (3 * 5 = 15) est compté deux fois
    sommeTotale = int(sommeMultiple(3) + sommeMultiple(5) - sommeMultiple(15))

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(sommeTotale, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 233168 , en : 0 ns.

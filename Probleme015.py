import time
import Utilitaire

# Résumé : Grace à la fonction "combinaison",
# on calcule possibilité de choisir 20 chemins vers le bas parmi les (20 * 2 =) 40 possibilités.
# Une fois les chemins vers le bas choisis, les chemins vers la droites sont à chaque fois les chemins non choisis.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    nb = 20
    reponse = Utilitaire.combinaison(20 * 2, 20)

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(reponse, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 137846528820 , en : 0 ns.

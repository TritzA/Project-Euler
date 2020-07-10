import time

from Utilitaire import Gene

# Résumé : Grace à la fonction "combinaison",
# on calcule possibilité de choisir 20 chemins vers le bas parmi les (20 * 2 =) 40 possibilités.
# Une fois les chemins vers le bas choisis, les chemins vers la droites sont à chaque fois les chemins non choisis.
if __name__ == '__main__':
    temps_debut = time.time()

    nb = 20
    reponse = Gene.combinaison(20 * 2, 20)

    temps_fin = time.time()
    Gene.rep(reponse, temps_fin - temps_debut)
    # Réponse : 137846528820 , en : 0.000 s.

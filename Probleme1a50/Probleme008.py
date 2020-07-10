import time

from Utilitaire import Gene

# Résumé : Parcours la chaine de caratères en incrémentant la multiplication de 13 nombres
# à la fois en conservant le plus grand produit. Si l'itérateur arrive sur un 0,
# il passe tous les produits possibles contenant ce dernier.
if __name__ == '__main__':
    temps_debut = time.time()

    taille_produit = 13
    chaine_nombre = Gene.lire("Probleme008")
    produit_max = 0
    i = 0

    while i < len(chaine_nombre) - (taille_produit - 1):

        produit_temporaire = 1
        j = 0
        presence_zero = False

        while j < taille_produit and not presence_zero:
            if produit_temporaire == 0:
                presence_zero = True  # sort de la boucle si croise un 0
                i += 2 * taille_produit - 2  # passe la section où il y a un 0
            else:
                produit_temporaire *= int(chaine_nombre[i + j])  # sinon continue sa recherche de 0
                j += 1

        if produit_max < produit_temporaire:
            produit_max = produit_temporaire  # si trouve un plus grand produit
        i += 1

    temps_fin = time.time()
    Gene.rep(produit_max, temps_fin - temps_debut)
    # Réponse : 23514624000 , en : 0.001 s.

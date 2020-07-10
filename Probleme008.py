import time

import Uti


def lire_nombre():
    return "73167176531330624919225119674426574742355349194934" \
           "96983520312774506326239578318016984801869478851843" \
           "85861560789112949495459501737958331952853208805511" \
           "12540698747158523863050715693290963295227443043557" \
           "66896648950445244523161731856403098711121722383113" \
           "62229893423380308135336276614282806444486645238749" \
           "30358907296290491560440772390713810515859307960866" \
           "70172427121883998797908792274921901699720888093776" \
           "65727333001053367881220235421809751254540594752243" \
           "52584907711670556013604839586446706324415722155397" \
           "53697817977846174064955149290862569321978468622482" \
           "83972241375657056057490261407972968652414535100474" \
           "82166370484403199890008895243450658541227588666881" \
           "16427171479924442928230863465674813919123162824586" \
           "17866458359124566529476545682848912883142607690042" \
           "24219022671055626321111109370544217506941658960408" \
           "07198403850962455444362981230987879927244284909188" \
           "84580156166097919133875499200524063689912560717606" \
           "05886116467109405077541002256983155200055935729725" \
           "71636269561882670428252483600823257530420752963450"


# Résumé : Parcours la chaine de caratères en incrémentant la multiplication de 13 nombres
# à la fois en conservant le plus grand produit. Si l'itérateur arrive sur un 0,
# il passe tous les produits possibles contenant ce dernier.
if __name__ == '__main__':
    temps_debut = time.time()

    taille_produit = 13
    chaine_nombre = lire_nombre()
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
    Uti.rep(produit_max, temps_fin - temps_debut)
    # Réponse : 23514624000 , en : 0.001 s.

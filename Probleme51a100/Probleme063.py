import time

from Utilitaire import Gene

# Résumé : On parcourt les bases et les exposants,
# on incrémente le compteur lorsque la propriété est validée.
if __name__ == '__main__':
    temps_debut = time.time()

    cmpt = 0
    for base in range(1, 10):

        debut = False  # on n'a pas encore commencé à trouver des nombres qui valident la propriété
        pas_fin = True  # condition de la boucle qui fait varier l'exposant
        exposant = 0

        while pas_fin:
            exposant += 1
            taille = len(str(base ** exposant))

            if taille == exposant:
                debut = True
                cmpt += 1

            elif debut:
                pas_fin = False

    temps_fin = time.time()
    Gene.rep(cmpt, temps_fin - temps_debut)
    # Réponse : 49 , en : 0.000 s.

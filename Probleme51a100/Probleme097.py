import time

from Utilitaire import Gene

# Résumé : On effectue la puissance en conservant à chanque fois seulement des 10 derniers chiffres du nombre.
if __name__ == '__main__':
    temps_debut = time.time()

    nb = 1
    for i in range(1, 7830458):
        nb = int(str(2 * nb)[-10:])
    nb *= 28433
    nb = str(nb + 1)
    fin = nb[-10:]

    temps_fin = time.time()
    Gene.rep(fin, temps_fin - temps_debut)
    # Réponse : 8739992577 , en : 8.988 s.

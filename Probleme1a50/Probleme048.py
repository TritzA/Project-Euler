import time

from Utilitaire import Gene

# Résumé : On parcourt la suite en incrémentant chaque terme.
# Ensuite, on conserve uniquement les 10 derniers chiffres de la série.
# Le calcul de Sn de la suite n ^ n nous mènerait à une solution constante de O(1),
# mais je ne sais pas si une telle formule existe.
if __name__ == '__main__':
    temps_debut = time.time()

    somme = 0
    for i in range(1, 1000):
        somme += i ** i
    somme = str(somme)
    somme = somme[len(somme) - 10:]

    temps_fin = time.time()
    Gene.rep(somme, temps_fin - temps_debut)
    # Réponse : 9110846700 , en : 0.041 s.

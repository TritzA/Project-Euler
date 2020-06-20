import time
import Utilitaire

# Résumé : On passe à travers les nombres de 2 à 10000
# exclu en charchant si chaque nombre à un nombre ami.
if __name__ == '__main__':
    temps_debut = time.time_ns()

    somme = 0
    a = 2
    while a < 10000:
        b = Utilitaire.somme_diviseurs(a)
        if Utilitaire.somme_diviseurs(b) == a and a != b:
            somme += a
        a += 1

    temps_fin = time.time_ns()
    Utilitaire.afficher_reponse(somme, Utilitaire.fin_temps(temps_debut, temps_fin))
    # Réponse : 31626 , en : 9781.6437 ms.

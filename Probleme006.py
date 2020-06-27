import time
import Uti

# Résumé : On effectue la somme des carrés puis le carré de la somme,
# puis on calcule la différence entre le deuxième et le premier.
if __name__ == '__main__':
    temps_debut = time.time()

    fin = 100
    somme_carre = fin * (fin + 1) * (2 * fin + 1) // 6
    carre_somme = (fin * (fin + 1) / 2) ** 2
    rep = int(carre_somme - somme_carre)

    temps_fin = time.time()
    Uti.rep(rep, temps_fin - temps_debut)
    # Réponse : 25164150 , en : 0.000 s.

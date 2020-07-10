import time

from Utilitaire import Gene

# Résumé : On conserve dans une chaîne les nombres jusqu'à un demi-million.
# Ensuite, on multiplie les chiffres recherchés dans ces décimales.
if __name__ == '__main__':
    temps_debut = time.time()

    nombre = "0"
    for i in range(1, 1000000 // 2):
        nombre += str(i)

    produit = 1
    for i in range(1, 7):
        produit *= int(nombre[10 ** i])

    temps_fin = time.time()
    Gene.rep(produit, temps_fin - temps_debut)
    # Réponse : 210 , en : 1.870 s.

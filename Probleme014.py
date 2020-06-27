import time
import Uti

valeurs = {1: 0}


def sequence(n):
    global valeurs
    if n in valeurs:
        return valeurs[n]

    if n % 2 == 0:
        valeurs[n] = 1 + sequence(n // 2)
    else:
        valeurs[n] = 2 + sequence((3 * n + 1) // 2)
    return valeurs[n]


# Résumé : On passe à travers les nombres de 500K à 1M-1 inclusivement
# (ces nombres passeront forcément par les nombres de 1 à 500k-1, ils n'ont donc pas besoin d'être testés en plus).
# Aussi, on stock les longueur de Collatz qu'on obtient pour éviter de les comter deux fois.
# En plus, on effectue deux opérations d'un coup losqu'on tombe sur un nombre impaire
# étant donné qu'après la première opération on tombera forcément sur un nombre pair.
if __name__ == '__main__':
    temps_debut = time.time()

    max = 0
    for i in range(1000000 // 2, 1000000):
        tempo = sequence(i)
        if max < tempo:
            max = tempo
            reponse = i

    temps_fin = time.time()
    Uti.rep(reponse, temps_fin - temps_debut)
    # Réponse : 837799 , en : 1.748 s.

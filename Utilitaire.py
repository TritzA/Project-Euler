import math


def fin_temps(temps_debut, temps_fin):
    temps = temps_fin - temps_debut
    if str(temps)[0] == '0':
        return temps
    else:
        return temps / math.pow(10, 6)


def afficher_reponse(reponse, temps):
    if str(temps)[0] == '0':
        print("# Réponse :", reponse, ", en :", temps, "ns.")
    else:
        print("# Réponse :", reponse, ", en :", temps, "ms.")


def est_premier(n):
    if n == 1:
        return False
    elif n < 4:
        return True  # 2 et 3 sont premiers
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True  # 4,6 et 8 sont déjà inclu
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))  # sqrt (n) arrondi au plus grand entier r de sorte que r * r <= n
        f = 5
        while f <= r:
            if n % f == 0:
                return False  # sort de la fonction
            if n % (f + 2) == 0:
                return False  # sort de la fonction
            f += 6
    return True  # dans tous les autres cas


def taille(nb):
    return len(str(int(nb)))

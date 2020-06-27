import math
import Uti


def premier(n):
    if n < 2:
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


def parfait(n):
    if sum(Uti.diviseurs(n)) == n:
        return True
    else:
        return False


def abondant(n):
    if n == 1:
        return False
    elif n == 2:
        return False
    elif sum(Uti.diviseurs(n)) > n:
        return True
    else:
        return False


def deficient(n):
    if sum(Uti.diviseurs(n)) < n:
        return True
    else:
        return False


def amical(n):
    ami = sum(Uti.diviseurs(n))
    if sum(Uti.diviseurs(ami)) == n and ami != n:
        return True
    return False


def triangulaire(n):
    racine = math.sqrt(8 * n + 1)
    arrondi = math.floor(racine)
    if racine == arrondi:
        return True
    return False


def palindrome(nb):
    nb = str(nb)
    k = 0
    while k < len(nb) // 2:
        if nb[k] != nb[len(nb) - (k + 1)]:
            return False
        k += 1
    return True

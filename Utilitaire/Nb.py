import math

from Utilitaire import Gene


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


def compose(n):
    if premier(n):
        return False
    return True


def parfait(n):
    if sum(Gene.diviseurs(n)) == n:
        return True
    else:
        return False


def abondant(n):
    if n == 1:
        return False
    elif n == 2:
        return False
    elif sum(Gene.diviseurs(n)) > n:
        return True
    else:
        return False


def deficient(n):
    if sum(Gene.diviseurs(n)) < n:
        return True
    else:
        return False


def amical(n):
    ami = sum(Gene.diviseurs(n))
    if sum(Gene.diviseurs(ami)) == n and ami != n:
        return True
    return False


def triangulaire(n):
    racine = math.sqrt(8 * n + 1)
    arrondi = math.floor(racine)
    if racine == arrondi:
        return True
    return False


def pentagonal(n):
    if (1 + math.sqrt(24 * n + 1)) % 6 == 0:
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


def pandigital(chaine, n=9):
    if len(chaine) != n:
        return False
    for i in range(1, n + 1):
        if str(i) in chaine:
            chaine = chaine.replace(str(i), "")
        else:
            return False
    return True

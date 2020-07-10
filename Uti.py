import math


def rep(reponse, temps):
    temps = str(temps)
    if len(temps) == 3:
        temps += "00"
    else:
        str(temps)[:5]
    pnt = temps.index('.')
    print("# Réponse :", reponse, ", en :", str(temps)[:pnt] + str(temps)[pnt:pnt + 4], "s.")


def combinaison(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def permutation(n, k):
    return math.factorial(n) // math.factorial(n - k)


def diviseurs(nb, extremum=False):  # Code internet à revoir
    divisors = [1]
    inf = 1 if extremum else 2
    for i in range(inf, int(nb ** 0.5) + 1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb // i)
    return divisors


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):  # Code internet à revoir
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


def lire(nom_fichier):
    mon_fichier = open("Fichiers/" + nom_fichier, "r")
    contenu = mon_fichier.read()
    mon_fichier.close()
    return contenu

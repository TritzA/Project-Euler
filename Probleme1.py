if __name__ == '__main__':

    nb = 1
    somme = 0
    while nb < 1000:
        if nb % 3 == 0:
            somme += nb
        elif nb % 5 == 0:
            somme += nb
        nb += 1
    print("Response : ", somme)

# ctrl+alt+l clean code

def estPremier(nb):
    cmpt = 2
    premier = True
    # if cmpt%2 == 0:
    #    premier = False
    # else:
    #    cmpt+=1

    while cmpt < int(nb / 2) + 1 and premier:
        if nb % cmpt == 0:
            premier = False
        cmpt += 1
    return premier


def plus_petit_facteur_premier(nb):
    trouve = False
    cmpt = 2
    while not trouve:
        if nb % cmpt == 0:
            return cmpt
        else:
            cmpt += 1


if __name__ == '__main__':
    nombre = 600851475143
    cmpt = 2
    max = 0
    trouve = False
    if nombre % cmpt == 0:
        trouve = True
    else:
        cmpt += 1
    while not estPremier(nombre):
        while not trouve:
            if nombre % cmpt == 0 and estPremier(cmpt):
                print("Facteur premier : ", cmpt)
                if cmpt < max:
                    max = cmpt
                trouve = True
            else:
                cmpt += 2
        nombre = nombre/cmpt
        print("Nouveau nombre : ", nombre)
        trouve = False
    print("Reponse : ", nombre)

if __name__ == '__main__':
    estPremier(29)

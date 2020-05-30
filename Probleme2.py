if __name__ == '__main__':
    nbUn = 1
    nbDeux = 2
    somme = 2
    tempo = 0
    while nbUn < 4000000:
        tempo = nbUn
        nbUn = nbDeux
        nbDeux = nbDeux + tempo
        if(nbDeux % 2 == 0):
            somme += nbDeux
    print("Reponse : ", somme)
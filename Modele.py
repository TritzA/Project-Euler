import time
import math


def fin_temps(temps_initial):
    temps_final = time.time_ns()
    print(math.pow(10, 6))
    return (temps_final - temps_initial) * math.pow(10, 6)


# Resume :
if __name__ == '__main__':
    temps_initial = time.time_ns()

    ### CODE ICI

    temps_fin = time.time()
    reponse = -1
    print("Reponse : ", reponse, ", en : ", fin_temps(temps_initial), "ms")

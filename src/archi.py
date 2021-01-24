##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## archi.py
##

from src.calc import *
from src.vector import *

def fill_matrice(matrice_tmp, matrice, c):
    if (c == 1):
        for a in matrice:
            matrice_tmp.append(a)
    elif (c >= 2):
        matrice_tmp = matrice_mult(matrice_tmp, matrice)
    return matrice_tmp

def archi(vector, matrice_tmp, av, i):
    c = 0
    while i < len(av):
        matrice = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        if (av[i] == '-r'):
            matrice = matrice_r(matrice, int(av[i + 1]))
            vector = vector_rs(matrice, vector)
        elif (av[i] == '-s'):
            matrice = matrice_s(matrice, int(av[i + 1]))
            vector = vector_rs(matrice, vector)
        elif (av[i] == '-t'):
            matrice = matrice_t(matrice, int(av[i + 1]), int(av[i + 2]))
            vector = vector_t(vector, float(av[i + 1]), float(av[i + 2]))
        elif (av[i] == '-z'):
            matrice = matrice_z(matrice, int(av[i + 1]), int(av[i + 2]))
            vector = vector_z(vector, float(av[i + 1]), float(av[i + 2]))
        c += 1 if (av[i] == '-r' or av[i] == '-s' or av[i] == '-z' or
            av[i] == '-t') else 0
        i += 3 if (av[i] == '-t' or av[i] == '-z') else 2
        matrice_tmp = fill_matrice(matrice_tmp, matrice, c)
    print_matrice(matrice_tmp)
    return vector
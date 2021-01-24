##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## calc.py
##

import math
from src.vector import vector
from src.print import *

def matrice_mult(matrice, matrice_tmp):
	matrice_f = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	matrice_f[0] = (matrice_tmp[0] * matrice[0]) + (matrice_tmp[1] * matrice[3]) + (matrice_tmp[2] * matrice[6])
	matrice_f[1] = (matrice_tmp[0] * matrice[1]) + (matrice_tmp[1] * matrice[4]) + (matrice_tmp[2] * matrice[7])
	matrice_f[2] = (matrice_tmp[0] * matrice[2]) + (matrice_tmp[1] * matrice[5]) + (matrice_tmp[2] * matrice[8])
	matrice_f[3] = (matrice_tmp[3] * matrice[0]) + (matrice_tmp[4] * matrice[3]) + (matrice_tmp[5] * matrice[6])
	matrice_f[4] = (matrice_tmp[3] * matrice[1]) + (matrice_tmp[4] * matrice[4]) + (matrice_tmp[5] * matrice[7])
	matrice_f[5] = (matrice_tmp[3] * matrice[2]) + (matrice_tmp[4] * matrice[5]) + (matrice_tmp[5] * matrice[8])
	matrice_f[6] = (matrice_tmp[6] * matrice[0]) + (matrice_tmp[7] * matrice[3]) + (matrice_tmp[8] * matrice[6])
	matrice_f[7] = (matrice_tmp[6] * matrice[1]) + (matrice_tmp[7] * matrice[4]) + (matrice_tmp[8] * matrice[7])
	matrice_f[8] = (matrice_tmp[6] * matrice[2]) + (matrice_tmp[7] * matrice[5]) + (matrice_tmp[8] * matrice[8])
	return matrice_f

def matrice_r(matrice, av):
    rotation(av)
    matrice[0] = math.cos(math.radians(av))
    matrice[1] = -math.sin(math.radians(av))
    matrice[3] = math.sin(math.radians(av))
    matrice[4] = math.cos(math.radians(av))
    return matrice

def matrice_s(matrice, av):
    reflection(av)
    matrice[0] = math.cos(2 * math.radians(av))
    matrice[1] = math.sin(2 * math.radians(av))
    matrice[3] = math.sin(2 * math.radians(av))
    matrice[4] = -math.cos(2 * math.radians(av))
    return matrice

def matrice_t(matrice, av, av2):
    translation(av, av2)
    matrice[0] = 1
    matrice[2] = av
    matrice[4] = 1
    matrice[5] = av2
    return matrice

def matrice_z(matrice, av, av2):
    scaling(av, av2)
    matrice[0] = av
    matrice[4] = av2
    return matrice
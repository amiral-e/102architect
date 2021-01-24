#!/usr/bin/python3

##
## EPITECH PROJECT, 2020
## 102architect
## File description:
## 102architect main file
##

import os
import math
import random
from sys import argv
from src.constants import NB_ARGS_MIN, NB_ARGS_MAX
from src.errors_man import errors
from src.archi import *
from src.print import final
from src.vector import vector
from src.calc import *

def check_flags(ac, av):
    i = 3
    while i < ac:
        if (av[i] == '-r' or av[i] == '-s'):
            float(av[i + 1])
            i += 2
        elif (av[i] == '-t' or av[i] == '-z'):
            float(av[i + 1])
            float(av[i + 2])
            i += 3
        else:
            exit(errors(4, ac))

def main(ac, av):
    if (ac == 1 or (ac == 2 and av[1] == "-h")):
        exit(errors(1, ac))
    elif (ac != 3 and (ac < 5 or ac > 11) and ac != 13):
        exit(errors(2, ac))
    matrice_tmp = []
    try:
        check_flags(ac, av)
        vect = archi(vector(float(av[1]), float(av[2])), matrice_tmp, av, 3)
        final(float(av[1]), float(av[2]), vect)
    except ValueError:
        exit(errors(3, ac))
    except IndexError:
        exit(errors(2, ac))

ac = len(argv)
main(ac, argv)

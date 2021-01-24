##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## errors_man.py
##

import os
from sys import argv
import math
import random
from src.constants import *

def usage(c):
    if (c == 1):
        print("Usage: ./102architect -h")
    else:
        print("USAGE\n    ./102architect x y transfo1 arg11 [arg12] [transfo2 arg12 [arg22]] ...\n")
        print("DESCRIPTION")
        print("    x  abscissa of the original point")
        print("    y  ordinate of the original point\n")
        print("    transfo arg1 [arg2]")
        print("    -t i j  translation along vector (i, j)")
        print("    -z m n  scaling by factors m (x-axis) and n (y-axis)")
        print("    -r d    rotation centered in O by a d degree angle")
        print("    -s d    reflection over the axis passing through O with an inclination\n\t    angle of d degrees")

def errors(c, num_arg):
    if (c == 1):
        if (num_arg == 1):
            usage(1)
        elif (num_arg == 2):
            usage(2)
            return (0)
    elif (c == 2):
        print(INVALID_NB_ARGS)
    elif (c == 3):
        print(INVALID_ARG)
    elif (c == 4):
        print(INVALID_FLAG)
    elif (c == 5):
        print(DUP_FLAG)
    return (84)

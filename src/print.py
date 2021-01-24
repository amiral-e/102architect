##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## print.py
##

def translation(i, j):
    print("Translation along vector (", i, ", ", j, ")", sep = "")

def scaling(m, n):
    print("Scaling by factors ", m, " and ", n, sep = "")

def rotation(angle):
    print("Rotation by a ", int(angle), " degree angle", sep = "")

def reflection(angle):
    print("Reflection over an axis with an inclination angle of ", angle, " degrees", sep = "")

def print_matrice(matrice):
    print("%.2f" % matrice[0], "%.2f" % matrice[1], "%.2f" % matrice[2], sep = "\t")
    print("%.2f" % matrice[3], "%.2f" % matrice[4], "%.2f" % matrice[5], sep = "\t")
    print("%.2f" % matrice[6], "%.2f" % matrice[7], "%.2f" % matrice[8], sep = "\t")

def final(x, y, vector):
    print("(%.2f," % x, "%.2f)" % y, "=> (%.2f," % vector.x, "%.2f)" % vector.y)
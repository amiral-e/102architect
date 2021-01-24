##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## vector.py
##

class vector:
    def __init__(self, x:float = 0.00, y:float = 0.00):
        self.x = x
        self.y = y

def vector_rs(matrice, vector):
    save = (vector.x * matrice[0]) + (vector.y * matrice[1])
    vector.y = (vector.x * matrice[3]) + (vector.y * matrice[4])
    vector.x = save
    return vector

def vector_t(vector, av, av2):
    vector.x += av
    vector.y += av2
    return vector

def vector_z(vector, av, av2):
    vector.x *= av
    vector.y *= av2
    return vector
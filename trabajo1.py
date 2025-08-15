import numpy as np
from itertools import permutations

def iso(A,B): 
    dim = list(A.shape)[0] #Dimensión de la matriz
    I = np.eye(dim)
    p = list(permutations(np.arange(0,dim)))
    encontro = False
    for i in range(0,len(p)):
        I = I[list(p[i])]
        if ((I@A)@I.T == B).all() == True:
           encontro = True
           print(f"La matriz de permutación es:\n {I}")
           return I
    if encontro == False:
        print("No se encontro matriz de permutación")
        
#EJEMPLO 1
x = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
])
z = np.array([
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
])

#A = iso(x,z)

#EJEMPLO 2 (El de la tarea)
U = np.array([
    [0, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]
])
U = U + U.T

V = np.array([
    [0, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]
])
V = V + V.T

B = iso(U,V)

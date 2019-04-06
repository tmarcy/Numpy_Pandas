"""
BROADCASTING
operazioni vettoriali sugli array
"""
import numpy as np

# e' possibile effettuare operazioni aritmetiche vettoriali tra arry numpy
# che hanno la stessa forma

a = np.arange(4)
b = np.arange(1, 5)

print('a')
print(a)
print('b')
print(b)
print('a + b')
print(a+b)

# moltiplicazione per lo scalare 5 di ogni elemento dell'array
# diversamente da come accade in python
print(a*5)
seq = [1, 2, 3]
print(seq*5)

# somma tra un vettore e una matrice
# il vettore viene adattato alle dimensioni della matrice
# in questo caso il vettore v di dimensioni (1, 3)
# v viene replicato fino a diventare una matrice di dimensioni (3,3)
matrix = np.arange(1, 10).reshape(3, 3)
print('matrix')
print(matrix)

v = np.array([1, 1, 1], dtype=int)
print('matrix + v')
print(matrix + v)

# prodotto scalare tra due vettori
# il risultato e' un numero
v1 = [1, 2, 3]
v2 = [4, 5, 6]
ps12 = np.dot(v1, v2)
print('ps12: {}'.format(ps12))

# prodotto scalare tra matrice e vettore
ps = np.dot(matrix, v)
sp = np.dot(v, matrix)
print('ps')
print ps
print('sp')
print sp

# somma di tutti gli elementi della matrice
print('sum matrix elements')
print(np.sum(matrix))

# e' possibile operare sui singoli vettori riga o vettori colonna
# che compongono la matrice utilizzandoun singolo parametro: axis
print('sum matrix rows elements')
print(np.sum(matrix, axis=1))
print('sum matrix columns elements')
print(np.sum(matrix, axis=0))

print('mean matrix rows elements')
print(np.mean(matrix, axis=1))

print('max matrix columns elements')
print(np.max(matrix, axis=0))

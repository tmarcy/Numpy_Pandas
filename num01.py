"""
Primi passi con NumPy
"""
import numpy as np

# inizializzazione

numbers = np.array([10, 20, 30, 40, 50], copy=True)

print('numbers: {}'.format(numbers))

# crea una matrice 2x4 di tutti 1
# accetta un param. obbligatorio: lista (o tupla) delle dimensioni dell'array
ones = np.ones([2, 4], dtype=np.float64)

# crea una matrice 2x4 di tutti 0
# accetta un param. obbligatorio: lista (o tupla) delle dimensioni dell'array
zeros = np.zeros([3, 4], dtype=np.float64)

# crea una matrice di elementi non inizializzati
# accetta un param. obbligatorio: lista (o tupla) delle dimensioni dell'array
empty = np.empty((2, 2), dtype=np.float32)

print('ones')
print(ones)
print('zeros')
print(zeros)
print('empty')
print(empty)

# numpy memorizza la dimensione, la forma e il tipo dei dati di un array

print('one\'s dim: {}, shape: {}, dtype:{}'.format(ones.ndim, ones.shape, ones.dtype))
print('numbers\' dim: {}, shape: {}, dtype:{}'.format(numbers.ndim, numbers.shape, numbers.dtype))

# La funzione eye(N, M, k, dtype) crea una matrice identita' sulla diagonale k-sima
# costruisce una matrice NxM, in cui gli elementi
# che si trovano sulla k-esima diagonale sono = 1, tutti gli altri sono = 0

eye = np.eye(3)  # matrice identita'
eye2 = np.eye(3, k=1)
eye3 = np.eye(3, 4, k=1)

# creazione di una matrice identita'
eye5 = np.identity(4, dtype=int)

print('eye')
print(eye)
print('eye2')
print(eye2)
print('eye3')
print(eye3)
print('eye5')
print(eye5)

# questo statement permette di ottenere gli stessi valori numerici ogni volta
# funziona a livello di blocco di codice
# https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do/21494630

np.random.seed(0)

a = np.random.rand(3,3)*10
print('a')
print(a)

b = np.random.randint(5, size=[3, 3])
print('b')
print(b)

np_numbers = np.arange(2, 5, 0.25, dtype=np.float32)
print('np_numbers')
print(np_numbers)

c = np.array(range(10), int)
d = np.arange(2, 8)
print('c')
print(c)
print('d')
print(d)

# intervalli numerici uniformmente distribuiti
e = np.linspace(0, 10, num=20)
print('e')
print(e)

# in questo modo l'assegnamento viene fatto per riferimento
v = np.array([1, 2, 3])
tmp = v[:2]
# in questo modo l'assegnamento viene fatto per copia
tmp = v[:2].copy()

print('v: {}'.format(v))
print('tmp: {}'.format(tmp))

# NaN:not a number
myvec = np.array([7, np.nan, 8, 9])
print('myvec_nan:{}'.format(myvec))
myvec[np.isnan(myvec)] = 0
print('myvec:{}'.format(myvec))
# in accordo con la tradizione dei dati scientific, si puo' usare nan
# come segnaposto per i dati mancanti

# Altri metodi
# nonzero() restituisce gli indici di tutti gli elementi diversi da 0
print(np.nonzero(myvec))

# any() restituisce True se un elemento qualsiasi dell'array e' diverso da 0
print(np.any(myvec))

# all() restituisce True se tutti gli elementi dell'array sono diversi da zero
print(np.all(myvec))

# inserire, aggiungere, eliminare
# alla posizione con indice 2 inserisce l'elemento 10
# tutti gli altri elementi shiftano
v = np.insert(v, 2, 10)
print(v)

# inserisce il numero come ultimo elemento
v = np.append(v, 20)
print(v)

# elimina l'elemento in posizione 2
v = np.delete(v, 2)
print(v)


# ordina il vettore in ordine crescente
print(np.sort(v))

# funzioni statistiche
print(np.min(v))
print(np.max(v))
print(np.mean(v))
print(v.min())
print(v.max())
print(v.argmin())
print(v.std())

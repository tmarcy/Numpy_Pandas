"""
Indicizzazione e slicing.
Esempi di Data cleaning
Per ripulire i dati sporchi, bisogna individuare i valori errati
e sostituirli con alternative ragionevoli.
"""
import numpy as np

dirty = np.array([10, 20, 30, -5, -4, 40, 50, -2, 0])

# Esempio di indicizzazione booleana
# I dati devono essere assolutamente non negativi

# MASCHERA: whos_dirty
# lista di valori booleani
# seleziona solo i valori del vettore che soddisfano una certa condizione
whos_dirty = (dirty < 0)

# per applicare la maschera, la passo come se fosse un indice
# i valori che corrispondono a "vero" nella maschera verranno selezionati
# e gli sara' assegnato il valore 0
dirty[whos_dirty] = 0

print(whos_dirty)
print(dirty)

mylist = np.arange(-1, 1.1, 0.2)
print(mylist)
# Quali elementi della lista sono compresi tra -0.5 e 0.5?
print((mylist <= 0.5) & (mylist >= -0.5))

# Slicing intelligent array o lista di indici come indice
# il risultato della selezione e' l'array degli elementi individuato dall'indice

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])
print(sap[[1, 2, -1]])

sap2d = sap.reshape(2, 4)

print('sap2d')
print(sap2d)

# Estrazione di tutte le righe della colonna centrale
# assicurarsi sempre di ottenere quello che si desidera!
print('bidimensionale')
print(sap2d[:, [1]])  # matrice bidimensionale
# assicurarsi sempre di ottenere quello che si desidera!
print('monodimensionale')
print(sap2d[:, 1])  # array monodimensionale

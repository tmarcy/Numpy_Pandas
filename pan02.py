"""
Dataset Iris
"""
import pandas as pd

iris = pd.read_excel("/home/marcella/Scaricati/Iris.xls")

# il file viene caricato all'interno della struttura dati DataFrame
# prime e ultime 10 righe del dataset
print iris.head(10)
print iris.tail(10)

print("colonne")
print(iris.columns)

print("informazioni")
iris.info()

# si accede0 ai nomi delle colonne utilizzando le chiavi
y = iris['petal width']
print(y.head())

# informazioni di tipo statistico sul dataset
print(iris.describe())

# estrarre dati da un dataframe usando gli indici numerici
print('Estrazione dei dati contenuti nella prima riga')
print(iris.iloc[0])

# slicing del dataset: seleziono solo alcune righe e/o alcune colonne
print('Estrazione delle righe contenute nell\'intervallo [100, 110[')
print(iris.iloc[100:110])

# creare un dataset piu' piccolo
iris_mini = iris.iloc[100:, 2:4]
print('iris_mini')
print(iris_mini)

# estrarre dati mediante etichetta (tipo dizionario)
print('Estrazione dei dati contenuti nella prima riga')
print(iris_mini.loc[100])

print('Elimino l\'ultima riga')
iris_mini = iris_mini.drop(iris_mini.index[len(iris_mini)-1])
print(iris_mini)

print('prima riga')
print(iris_mini.iloc[0])
print(iris_mini.loc[100])
print('Elimino la prima riga')
iris_mini = iris_mini.drop(iris_mini.index[0])
print(iris_mini)
print('prima riga')
# riga con indice 0
print(iris_mini.iloc[0])
# riga che si chiama 101
print(iris_mini.loc[101])

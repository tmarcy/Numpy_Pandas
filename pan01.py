"""
Pandas - Series e DataFrame
"""
import pandas as pd
import numpy as np

# Series ##############################################################################################################

inflation = pd.Series((2.2, 3.4, 2.8, 1.6, 2.3, 2.7, 3.4, 3.2, 2.8, 3.8, -0.4, 1.6, 3.2, 2.1, 1.5, 1.5))
print('values: {}'.format(inflation))
print('len values: {}').format(len(inflation))

print('values: {}').format(inflation.values)
print('index: {}'.format(inflation.index))
print('array dei valori indice: {}'.format(inflation.index.values))

inflation.values[-1] = 1.6
print('values: {}'.format(inflation))

# creo una serie passando un dizionario al costruttore
# le chiavi del dizionario diventano gli indici della serie

inflation = pd.Series({'1999': 2.2, '2000': 3.4, '2001': 2.8, '2002': 1.6, '2003': 2.3, '2004': 2.7, '2005': 3.4,
                        '2006': 3.2, '2007': 2.8, '2008': 3.8, '2009': -0.4, '2010': 1.6,
                        '2011': 3.2, '2012': 2.1, '2013': 1.5, '2014': 1.5, '2015': np.nan})

print('values: {}'.format(inflation))

# in alternativa si puo' creare un nuovo indice da qualsiasi sequenza
# e poi collegarlo ad una serie esistente
inflation.index = pd.Index(range(1999, 2016))
inflation[2015] = np.nan

# etichettare gli indici e i valori della serie
inflation.index.name = 'Year'
inflation.name = '%'
print(inflation)

# prime 5 righe della serie
print(inflation.head())
# ultime 5 righe della serie
print(inflation.tail())
# prime 2 righe della serie
print(inflation.head(2))
# ultime 2 righe della serie
print(inflation.tail(2))

# DataFrame ###########################################################################################################

# creo un DataFrame passando un dizionario al costruttore
# le chiavi del dizionario diventano i nomi per le colonne
# e i valori (che devono essere sequenze) diventano i valori delle colonne
# in base all'approccio NumPy, l'indice del frame diventa l'asse 0 (verticale)
# e le colonne del frame diventano l'asse 1 (orizzontale)



films = pd.DataFrame({"Regista": ("Jon Favreau", "Ron Howard", "Ridley Scott"),
                         "Anno": (2008 , 2001, 2000),
                         "Genere": ("Fantascienza", "Drammatico", "Drammatico")},
                        index= ("Iron Man", "A Beautiful Mind", "Il gladiatore")
                        )


print(films)

# Assegnamento di un valore a tutte le righe di una colonna
# se la colonna non esiste viene creata
films["Incasso"] = 200000000
print(films)

# accedere alle colonne del Frame
# modalita' dizionario
print(films["Regista"].head(2))
# modalita' punto
print(films.Anno.tail(2))

# Si accede alla righe del Frame con l'attributo "indice di riga"
# che si comporta come un dizionario della serie di righe
# dove la chiave e' rappresentata dalle etichette dell'indice
print(films.ix["Iron Man"])

# Per ogni colonna e' possibile sapere il tipo di dato
print(films.dtypes)

# concatenazione: unire piu' dataframe

films2 = pd.DataFrame(
            {"Regista": ("Jon Favreau", "Ron Howard", "Ridley Scott"),
                         "Anno": (2008 , 2001, 2000),
                         "Genere": ("Fantascienza", "Drammatico", "Drammatico")},
                        index= ("Iron Man", "A Beautiful Mind", "Il gladiatore")
                        )
df1 = pd.DataFrame(
                    {
                        'Genere': [
                                    "Fantascienza",
                                    "Drammatico",
                                    "Drammatico"
                                ],

                        'Regista': [
                                    "Jon Favreau",
                                    "Ron Howard",
                                    "Ridley Scott"
                                 ]
                    },
                    index = ["Iron Man", "A Beautiful Mind", "Il gladiatore"])

df2 = pd.DataFrame(
                    {
                        'Genere': [
                                    "Drammatico",
                                    "Drammatico"
                                ],

                        'Regista': [
                                    "Morten Tyldun",
                                    "Alejandro Gonzalez Inarritu"
                                 ]
                    },
                    index = ["The Imitation Game", "Revenant"])

newd = pd.concat([df1, df2])
print(newd)

# aggiungo al dataset una nuova colonna, usando il parametro axis = 1
# che indica a Pandas di operare sulle colonne

df3 = pd.DataFrame({'Anno': [
                                2008,
                                2001,
                                2000,
                                2015,
                                2016
                            ]
                    },
                    index = ["Iron Man", "A Beautiful Mind", "Il gladiatore", "The Imitation Game", "Revenant"])

newd = pd.concat([newd, df3], axis=1)
print(newd)









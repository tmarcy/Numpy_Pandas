# Numpy_Pandas
Primi passi con le librerie Numpy e Pandas.

## Descrizione
Il tema è l'**analisi dei dati** attraverso il linguaggio di programmazione **Python**.  
Gli elementi che compongono la triade **Python-NumPy-Pandas** sono i fondamenti del *working environment* di questa disciplina; più nello specifico,Python è alla base di Numpy, che nasce come pacchetto per il calcolo scientifico, introducendo strutture dati e metodi più efficienti, in questo contesto, rispetto a quelli già esistenti. A sua volta, Pandas si serve di NumPy per manipolare i dati.  
La conoscenza di NumPy e Pandas è molto importante per la scienza dei dati e questa raccolta di esercizi si pone l'obiettivo di illustrare i comandi base delle librerie. Il *target* a cui si rivolgono è dunque rappresentato dal livello *beginner*.

## NumPy - Numerical Python
* pacchetto di funzioni molto efficienti e parallelizzabili che implementano operazioni numeriche ad alte prestazioni;
* struttura dati: **numpy array**, in cui tutti gli elementi sono di tipo omogeneo (non è consentito impiegare elementi aventi tipi di dati differenti).  
Gli array Numpy sono più compatti e veloci delle normali liste Python, in particolare nei casi di multidimensionalità. Essi supportano le stesse operazioni di indicizzazione e *slicing* delle liste Python e implementano anche l' **indicizzazione booleana** (permette di utilizzare come indice un array di valori booleani --> il risultato della selezione sarà un array di quegli elementi dell’array di partenza, per i quali l’indice booleano è True).  
I parametri che caratterizzano gli array Numpy sono i seguenti:
* ndim = dimensione dei dati;  
* shape = forma dei dati;  
* dtype = tipo dei dati.

## Pandas
* libreria che fornisce gli strumenti per l’analisi dei dati, utile per caricare, esplorare, manipolare i Dataset;
* opera sulla base di Numpy, in alcuni casi estendendone e reimplementandone le funzionalità;
* permette di caricare dati in diversi formati;
* aggiunge al ricco *set* di strutture dati di Python due nuovi *container*: **Series** e **DataFrame**.  
Serie = vettore omogeneo monodimensionale etichettato, ovvero indicizzato.  
DataFrame = tabella di righe (osservazioni) e colonne (*features*) etichettate; ogni colonna del DataFrame è una Serie.

## Riferimenti

* [NumPy](http://www.numpy.org/)
* [Pandas](https://pandas.pydata.org/)

## Nota Bene

Versione non definitiva.

## Autore
**Marcella Tincani** - [Marcella](https://github.com/tmarcy)

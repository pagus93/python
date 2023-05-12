# Scrivi un programma che richieda all'utente di inserire una stringa e che conti quante volte ogni lettera appare nella stringa.
# Il programma dovrebbe quindi creare un dizionario in cui le chiavi sono le lettere presenti nella stringa e i valori sono il numero di volte che ogni lettera appare
# esempio di input: "banana"; output: {'b':1, 'a':3, 'n':2}

testo = input("Buongiorno. Per piacere inserire una stringa: ")
lettere = set(testo)
num_lettere = len(lettere)
dizionario = dict()

for char in lettere:
    counter = 0
    for i in range(0,len(testo)):
        if testo[i] == char:
            counter += 1
    dizionario[char] = counter

print(dizionario)
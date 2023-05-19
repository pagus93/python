
# richiedere all'utente di inserire una stringa e contare quante volte ogni lettera appare nella stringa
# utilizzare un dizionario (chiavi: lettere presenti nella stringa; valori: numero di volte che ogni lettera appare)
# esempio di input: "banana"; output: {'b':1, 'a':3, 'n':2}

testo = input("Buongiorno. Per cortesia inserire una stringa: ")
lettere = set(testo) # uso il set lettere, che toglie le ripetizioni dalla stringa testo, come set di chiavi del dizionario
dizionario = dict()

for lettera in lettere: # ripeto questo ciclo per ogni lettera presente nel testo dato in input
    counter = 0
    for char in testo: # ciclo che conta quante volte la lettera scelta compare nel testo
        if char == lettera:
            counter += 1
    dizionario[lettera] = counter # aggiunge la coppia lettera: counter al dizionario

print(dizionario) # stampa il dizionario
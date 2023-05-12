
# programma per la gestione di un registro vendite
# permette di aggiungere le vendite di diversi prodotti e calcolare il totale delle vendite (per ogni prodotto)
# 1. aggiungere una vendita di un prodotto (si richiede nome, quantità e prezzo)
# 2. visualizzare il totale delle vendite per ogni prodotto presente nel registro

registro = dict()
flag = True

while flag:
    scelta = input("""Editor registro vendite:
1. aggiungi dati vendita
2. visualizza registro
3. visualizza totale incassi per prodotto
4. visualizza fatturato totale
0. esci
""")

    if scelta == '1':
        nome = input("Inserire il nome del prodotto: ")
        prezzo = input("Inserire il prezzo per unità (in €): ")
        quantita = input("Inserire la quantità venduta: ")
        registro[nome] = [prezzo, quantita]

    elif scelta == '2':
        print(registro)
    
    elif scelta == '3':
        nome = input("Inserire il nome del prodotto: ")
        prezzo = float(registro[nome][0])
        quantità = int(registro[nome][1])
        print("Il prodotto", nome, "ha incassato un totale di:", prezzo*quantità, "€")

    elif scelta == '4':
        fatturato = 0
        for nome in registro.keys():
            prezzo = float(registro[nome][0])
            quantità = int(registro[nome][1])
            fatturato += prezzo*quantità
        print(fatturato)

    elif scelta == '0':
        flag = False

    else:
        print("Errore: comando non riconosciuto")

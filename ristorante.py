
menu = dict()
flag = True

while flag:
    scelta = input("""Editor menu e ordini:
1. aggiungi un piatto al menu
2. cancella un piatto dal menu
3. visualizza il menu completo
4. aggiungi un ordine
5. calcola il conto
0. esci
""")

    if scelta == '1':
        nome = input("Inserire il nome del piatto da aggiungere: ")
        prezzo = input("Inserire il prezzo (in €): ")
        menu[nome] = prezzo

    elif scelta == '2':
        nome = input("Inserire il nome del piatto da cancellare: ")
        del menu[nome]
       
    elif scelta == '3':
        print(menu)

    elif scelta == '4':
        ordine = dict()
        nome = input("Inserire il nome del piatto: ")
        quantita = input("Inserire la quantità ordinata: ")
        ordine[nome] = quantita
    
    elif scelta == '5':
        conto = 0
        for nome in ordine.keys():
            prezzo = float(menu[nome])
            quantita = float(ordine[nome])
            conto += prezzo*nome
        print("Il conto è di", conto, "€")

    elif scelta == '0':
        flag = False

    else:
        print("Errore: comando non riconosciuto")

 
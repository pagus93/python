
# TASK: CREARE UN SISTEMA DI ORDINAMENTO AD OGGETTI
# SI POSSONO ORDINARE 4 PIATTI FISSI, MODIFICARE UN PIATTO, O AVERE IL CONTO
# OGNI PIATRTO, HA NOME è PREZZO
# SE CHIEDIAMO IL CFONTO, CI DEVE CHIEDERE NOME E COGNOME E POI STAMPARE IL TOTALE E PIATTI A SCHERMO
# POI RITORNIAMO AL MENU INIZIALE
# UN OGGETTO CHE è ORDINAZIONE
# QUALI PIATTI, QUANTO HO SPESSO, CHI HA SPESSO SARANNO GLI ATTIRIBUTI DEGLI OGGETTI

class Ordinazioni:
    piatti = ["Bigoli al ragù d'anatra", "Spaghetti alla pescatora", "Frittura di pesce", "Tagliata di manzo"]
    prezzi = [10, 15, 20, 25]
    menu = []
    for i in range(0,len(piatti)):
        menu.append({"piatto": piatti[i], "prezzo": prezzi[i]})

    cliente = ""
    ordini = []
    totale = 0

    def menu_modifica(scelta, menu, piatto_nuovo, prezzo_nuovo):
        for i in range(0, len(menu)):
            if scelta == i:
                menu[i] = {"piatto": piatto_nuovo, "prezzo": prezzo_nuovo}
        print("Menù aggiornato:", menu)
    
    def menu_ordina(scelta, menu, cliente, ordini):
        for i in range(0, len(menu)):
            if scelta == i:
                ordini.append(menu[i]["piatto"])
        # print("Ordinazione del cliente", cliente, "aggiornata:", ordini)
    
    def conto(menu, cliente, ordini, totale):
        for j in range(0,len(ordini)):
            for i in range(0,len(menu)):
                if menu[i]["piatto"] == ordini[j]:
                    totale += float(menu[i]["prezzo"])
        print("Totale conto del cliente", cliente + ":", totale)

ordinazione = Ordinazioni()

flag1 = False
while not flag1:
    scelta1 = input("""Premere 1 per aggiungere un piatto all'ordinazione.
Premere 2 per calcolare il conto.
Premere 3 per modificare un piatto del menù.
Premere 0 per uscire.

""")

    if scelta1 == "0":
        flag1 = True
    
    elif scelta1 == "1":
        ordinazione.cliente = input("""
Inserire cognome e nome del cliente: """)

        flag2 = False
        while not flag2:
            scelta2 = input("""
Scegliere il piatto da aggiungere all'ordinazione:
Premere 1 per ordinare """ + ordinazione.piatti[0] + """.
Premere 2 per ordinare """ + ordinazione.piatti[1] + """.
Premere 3 per ordinare """ + ordinazione.piatti[2] + """.
Premere 4 per ordinare """ + ordinazione.piatti[3] + """.
Premere 0 per salvare l'ordinazione e tornare al menù principale.

""")
            if scelta2 == "0":
                flag2 = True
                print("""
Ordinazione del cliente """ + ordinazione.cliente + """ aggiornata: """ + ordinazione.ordini)
            else:
                ordinazione.menu_ordina(scelta2, ordinazione.menu, ordinazione.cliente, ordinazione.ordini)
    
    elif scelta1 == "2":
        ordinazione.conto(ordinazione.menu, ordinazione.ordini, ordinazione.totale)
    
    elif scelta1 == "3":
        flag2 = False
        while not flag2:
            scelta2 = input("""
Scegliere il piatto da sostituire nel menù:
Premere 1 per sostituire""", ordinazione.piatti[0] + """.
Premere 2 per sostituire""", ordinazione.piatti[1] + """.
Premere 3 per sostituire""", ordinazione.piatti[2] + """.
Premere 4 per sostituire""", ordinazione.piatti[3] + """.
Premere 0 per tornare al menù principale.

""")
            if scelta2 == "0":
                flag2 = True
            else:
                piatto_nuovo = input("""
Inserire il nome del nuovo piatto: """)
                prezzo_nuovo = input("""
Inserire il prezzo in € del nuovo piatto: """)
                ordinazione.menu_modifica(scelta2, ordinazione.menu, piatto_nuovo, prezzo_nuovo)
    
    else:
        print("Errore: input non riconosciuto.")


class Ordinazioni:
    menu = [{"piatto": "Bigoli al ragù d'anatra", "prezzo": "10"}, {"piatto": "Spaghetti alla pescatora", "prezzo": "15"}, {"piatto": "Frittura di pesce", "prezzo": "20"}, {"piatto": "Tagliata di manzo", "prezzo": "25"}]
    cliente = "Mario Rossi"
    ordini = []
    totale = 0

    def menu_elimina(self, scelta, menu):
        for i in range(0, len(menu)):
            if scelta == i+1:
                del menu[i]
        return menu

    def menu_aggiungi(self, menu, piatto_nuovo, prezzo_nuovo):
        menu.append({"piatto": piatto_nuovo, "prezzo": prezzo_nuovo})

    def menu_modifica(self, scelta, menu, piatto_nuovo, prezzo_nuovo):
        for i in range(0, len(menu)):
            if scelta == i+1:
                menu[i] = {"piatto": piatto_nuovo, "prezzo": prezzo_nuovo}
        return menu
    
    def menu_ordina(self, scelta, menu, cliente, ordini):
        for i in range(0, len(menu)):
            if scelta == i+1:
                ordini.append(menu[i]["piatto"])
    
    def conto(self, menu, cliente, ordini, totale):
        for j in range(0,len(ordini)):
            for i in range(0,len(menu)):
                if menu[i]["piatto"] == ordini[j]:
                    totale += float(menu[i]["prezzo"])
        return totale

ordinazione = Ordinazioni()

flag1 = False
while not flag1:
    scelta1 = int(input("\nPremere 1 per aggiungere un'ordinazione.\nPremere 2 per calcolare il conto.\nPremere 3 per cancellare un piatto dal menù.\nPremere 4 per aggiungere un piatto al menù.\nPremere 5 per modificare un piatto del menù.\nPremere 0 per uscire.\n\n"))

    if scelta1 == 0:
        flag1 = True
    
    elif scelta1 == 1:
        ordinazione.cliente = input("\nInserire cognome e nome del cliente: ")

        flag2 = False
        while not flag2:
            print(f"\nScegliere il piatto da aggiungere all'ordinazione:")
            for i in range(0,len(ordinazione.menu)):
                print(f"Premere {i+1} per ordinare " + ordinazione.menu[i]["piatto"] + " (" + ordinazione.menu[i]["prezzo"] + "€).")
            print("Premere 0 per salvare l'ordinazione e tornare al menù principale.\n")

            scelta2 = int(input())
            if scelta2 == 0:
                flag2 = True
                print(f"\nOrdinazione del cliente {ordinazione.cliente} aggiornata:\n{ordinazione.ordini}")
            else:
                ordinazione.menu_ordina(scelta2, ordinazione.menu, ordinazione.cliente, ordinazione.ordini)
    
    elif scelta1 == 2:
        ordinazione.totale = ordinazione.conto(ordinazione.menu, ordinazione.cliente, ordinazione.ordini, ordinazione.totale)
        print(f"\nTotale conto del cliente {ordinazione.cliente}: {ordinazione.totale}€")
    
    elif scelta1 == 3:
        flag2 = False
        while not flag2:
            print(f"\nScegliere il piatto da cancellare dal menù:")
            for i in range(0,len(ordinazione.menu)):
                print(f"Premere {i+1} per cancellare " + ordinazione.menu[i]["piatto"] + ".")
            print("Premere 0 per tornare al menù principale.\n")

            scelta2 = int(input())
            if scelta2 == 0:
                flag2 = True
            else:
                ordinazione.menu = ordinazione.menu_elimina(scelta2, ordinazione.menu)

    elif scelta1 == 4:
        flag2 = False
        while not flag2:
            piatto_nuovo = input(f"\nInserire il piatto da aggiungere al menù: ")
            prezzo_nuovo = input(f"Inserire il prezzo del piatto aggiunto: ")
            ordinazione.menu = ordinazione.menu_aggiungi(ordinazione.menu, piatto_nuovo, prezzo_nuovo)
            scelta2 = input("\nPremere 1 per aggiungere un nuovo piatto.\nPremere 0 per tornare al menù principale.\n")
            if scelta2 == 0:
                flag2 = True

    elif scelta1 == 5:
        flag2 = False
        while not flag2:
            print(f"\nScegliere il piatto da sostituire nel menù:")
            for i in range(0,len(ordinazione.menu)):
                print(f"Premere {i+1} per sostituire " + ordinazione.menu[i]["piatto"] + ".")
            print("Premere 0 per tornare al menù principale.\n")

            scelta2 = int(input())
            if scelta2 == 0:
                flag2 = True
            else:
                piatto_nuovo = input("\nInserire il nome del nuovo piatto: ")
                prezzo_nuovo = input("Inserire il prezzo in € del nuovo piatto: ")
                ordinazione.menu = ordinazione.menu_modifica(scelta2, ordinazione.menu, piatto_nuovo, prezzo_nuovo)
    
    else:
        print("Errore: input non riconosciuto.")

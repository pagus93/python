
class Operazione:
    simbolo = ""
    numero1 = ""
    numero2 = ""
    risultato = ""

def somma(x,y):
    return float(x)+float(y)

def sottrazione(x,y):
    return float(x)-float(y)

def moltiplicazione(x,y):
    return float(x)*float(y)

lista = []

flag1 = True
while flag1:
    scelta = input("""
Premere 1 per eseguire un'operazione matematica elementare.
Premere 2 per stampare i risultati delle operazioni inserite.
Premere 3 per ripulire i risultati.
Premere 4 per uscire.
""")

    if scelta == '1':
        for i in range(0,3):
            
            flag2 = True
            while flag2:
                simbolo = input("Inserire l'operazione ('+', '-' o '*'): ")
                numero1 = input("Inserire il primo termine: ")
                numero2 = input("Inserire il secondo termine: ")
                if (simbolo not in ['+','-','*']):
                    print("Errore, input non riconosciuto.")
                else:
                    flag2 = False

            oggetto = Operazione()
            oggetto.simbolo = simbolo
            oggetto.numero1 = numero1
            oggetto.numero2 = numero2
            if oggetto.simbolo == '+':
                oggetto.risultato = somma(oggetto.numero1,oggetto.numero2)
            elif oggetto.simbolo == '-':
                oggetto.risultato = sottrazione(oggetto.numero1,oggetto.numero2)
            elif oggetto.simbolo == '*':
                oggetto.risultato = moltiplicazione(oggetto.numero1,oggetto.numero2)
            lista.append(oggetto)

            i += 1
        
        somma = 0
        for i in range(0,len(lista)):
            somma += lista[i].risultato
        print("La somma dei risultati delle 3 operazioni è:", somma)

    elif scelta == '2':
        if lista == []:
            print("Non ci sono risultati salvati.")
        else:
            for i in range(0,3):
                print(lista[i].numero1, lista[i].simbolo, lista[i].numero2, "=", lista[i].risultato)

    elif scelta == '3':
        lista = []

    elif scelta == '4':
        flag1 = False
    
    else:
        print("Errore, input non riconosciuto")

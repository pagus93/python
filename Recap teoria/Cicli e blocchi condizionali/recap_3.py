
# scrivere un programma che prenda una lista di numeri come input e rimuove i duplicati dalla lista,
# lasciando solo i valori "unici"; l'ordine degli elementi nella lista deve rimanere invariato

"""
stringa1 = input("Inserire una lista di numeri separati da una virgola (eventuali caratteri non numerici diversi dalla virgola saranno ignorati): ")
stringa2 = ""

for char in stringa1:
    if char in ['0','1','2','3','4','5','6','7','8','9', ',']:
        stringa2 += char
    
lista = stringa2.split(",")

print(f"Ho ripulito la stringa e rimosso eventuali duplicati dalla lista:", lista)
"""

stringa1 = input("Inserire una lista di numeri separati da uno o più caratteri non numerici: ")
stringa2 = ""

I = range(0,len(stringa1))
for i in I:
    if stringa1[i] in ['0','1','2','3','4','5','6','7','8','9']:
        stringa2 += stringa1[i]
    elif stringa1[i-1] in ['0','1','2','3','4','5','6','7','8','9']:
        stringa2 += " "
    
lista = stringa2.split(" ")

print(lista) # rimuovere i duplicati! 
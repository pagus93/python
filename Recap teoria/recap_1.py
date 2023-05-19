
class Calice: # la classe definisce un nuovo tipo di dato
    contenuto = "spritz" # questa riga il compilatore non la legge finché non viene istanziato un oggetto di tipo Calice

class Bottiglia:
    capacitàInLitri = 3

oggetto1 = Calice() # variabile di tipo Calice
oggetto2 = Bottiglia()
oggetto3 = Bottiglia()

print(oggetto1) # stampa la posizione in memoria di oggetto1
print(oggetto2)
print(oggetto3)
print(oggetto1.contenuto) # stampa la variabile contenuto dell'oggetto1
print(oggetto2.capacitàInLitri)

print(oggetto3==oggetto2) # dà false

oggetto1.contenuto = "vino bianco" # riassegna la variabile contenuto
print(oggetto1.contenuto)

oggetto2.capacitàInLitri = "due litri"
print(oggetto2.capacitàInLitri)

oggetto3 = oggetto2 # riassegna oggetto3 alla posizione in memora di oggetto2
print(oggetto3)
print(oggetto3==oggetto2) # ora dà true

oggetto3 = oggetto1 # funziona anche cambiando classe
print(oggetto3)


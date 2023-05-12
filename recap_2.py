
# prendere una frase in input e restituire un dizionario che conta quante volte ogni parola appare nella frase 

testo = input("Inserire una frase: ") + " "
dizionario = dict()
parola = ""

for char in testo:
    if char != " ":
        parola += char
    else:
        if parola not in dizionario.keys():
            dizionario[parola] = 1
            parola = ""
        else:
            dizionario[parola] += 1
            parola = ""

print(dizionario)

# 11- Andare a creare un sistema i ordinazione di ferie, che permetta sulla base di tre proposte di modificare i vari parametri
# di esse, spesa tempodiviaggio e vista mare (int, string, bool  ) e che poi stampi il tutto chiedendo conferma,
# in quest'esercizio dovrete usare almeno ( oggetto: utente con validazione  e SceltaFerie coi dati)

import random

class Dado:
    def __init__(self,facce):
        self.facce = facce
    def lancia(self):
        n = random.randint(1,self.facce)
        return n

def genera_password():
    char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    parola = ""
    for i in range(0,8):
        n = Dado(26).lancia()
        parola += char_list[n]
    return parola

lista_utenti = []
lista_ferie = []

class Utente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    password = genera_password()   

    def aggiungi(self):
        for i in range(0,len(lista_utenti)):
            if lista_utenti[i].nome == self.nome and lista_utenti[i].cognome == self.cognome:
                break
        else:
            lista_utenti.append(self)

class Ferie(Utente):
    def __init__(self, nome, cognome, spesa, durata, vista_mare):
        super().__init__(nome,cognome)    
        self.spesa = spesa
        self.durata = durata
        self.vista_mare = vista_mare
    
    def modifica(self,nome,cognome,spesa,durata,vista_mare):
        for j in range(0,len(lista_ferie)):
            if lista_ferie[j].nome == nome and lista_ferie[j].cognome == cognome:
                lista_ferie[j].spesa = spesa
                lista_ferie[j].durata = durata
                lista_ferie[j].vista_mare = vista_mare

flag1 = False
while not flag1:
    scelta1 = input("Benvenuto.\nInserisci 1 per effettuare il login.\nInserisci 2 per registrarti.\nInserisci 0 per uscire.\n")

    if scelta1 == "0":
        flag1 = True

    elif scelta1 == "1":
        nome = input("Inserisci il tuo nome: ")
        cognome = input("Inserisci il tuo cognome: ")
        password = input("Inserisci la tua password: ")

        for i in range(0,len(lista_utenti)):

            if lista_utenti[i].nome == nome and lista_utenti[i].cognome == cognome:

                if lista_utenti[i].password == password:
                    flag2 = False

                    while not flag2:
                        scelta2 = input("\nInserisci 1 per scegliere le tue ferie.\nInserisci 2 per modificare la scelta.\nInserisci 0 per uscire.")
                        
                        if scelta2 == "0":
                            flag2 = True
                        
                        elif scelta2 == "1":
                            spesa = int(input("Inserisci il tuo budget: "))
                            durata = input("Inserisci la durata della vacanza: ")
                            vista_mare = bool(input("Inserisci 1 se desideri vista mare, 0 altrimenti: "))
                            ferie = Ferie(nome,cognome,spesa,durata,vista_mare)
                            lista_ferie.append(ferie)

                        elif scelta2 == "2":
                            spesa = int(input("Inserisci il tuo budget: "))
                            durata = input("Inserisci la durata della vacanza: ")
                            vista_mare = bool(input("Inserisci 1 se desideri vista mare, 0 altrimenti: "))
                            ferie = Ferie(nome,cognome,spesa,durata,vista_mare)
                            ferie.modifica(nome,cognome,spesa,durata,vista_mare)
                            
                        else:
                            print("Errore: input non riconosciuto.")

                else:
                    print("Errore: password errata.")
                          
                break
        else:
            print("Errore: utente non trovato.")

    elif scelta1 == "2":
        nome = input("Inserisci il tuo nome: ")
        cognome = input("Inserisci il tuo cognome: ")
        utente = Utente(nome,cognome)
        utente.aggiungi()
        print(f"La tua password è: {utente.password}")

    else:
        print("Errore: input non riconosciuto.")

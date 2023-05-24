"""
Un'azienda ha bisogno di un app per gestione le proprie risorse umane-
Release 1.0: 
Bisogna integrare un sistema di registrazione dipendenti con funzionalità CRUD (aggiungere dipendenti, eliminarli, modificare le loro informazioni) e che generi automaticamente un report quando richiesto. 
Release 2.0:
Bisogna implementare una funzionalità di calcolo delle retribuzioni e della gestione ferie.

"""

"""
classe dipendenti
classe con lista dipendenti (oggetti), accesso con password per il ceo

switch menu, login, pw per dipendenti

Menu generale:
1 dipendente
2 gestore
3 esci

Menu dipendenti (1):
Chiedi nome, cognome, pw
- Visualizza ferie
- visualizza retribuzione
- visualizza report
- esci

Menu gestore (2):
Chiedi pw
- Aggiungi dipendente
- Modifica dipendente
- Rimuovi dipendente
- Genera report
- esci

Menu  modifica ...

ToDo
- aggiungere calcolo salario
- aggiungere controllo: esiste già un dipendente all'aggiunta?
- Roadmap
- risolvere bug

ROADMAP
modifica tutto
gestione permessi (ferie/ore uscita/malattia...)
unicita utente


"""
# Importa librerie
import random


# Setta variabili
lista_dipendenti = []
reparti = {1: "HR", 2: "ADMIN"}
admin_password = "12345678"
utente = -1


# -------------------------------------------- CLASSI --------------------------------------------------------


# Classe padre
class Persona:
    # attributi: nome, cognome, password
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def to_string(self):
        return f"nome: {self.nome}, cognome: {self.cognome}"


# Classe figlio
class Dipendente(Persona):
    password = ""
    primo_ingresso = True
    ore_Ferie = 0

    def __init__(self, nome, cognome, inquadramento_aziendale, reparto):
        super().__init__(nome, cognome)
        self.inquadramento_aziendale = inquadramento_aziendale
        self.reparto = reparto

    def genera_password(self, n):
        self.password = ""
        char_list = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "A",
            "a",
            "B",
            "b",
            "C",
            "c",
            "D",
            "d",
            "E",
            "e",
            "F",
            "f",
            "G",
            "g",
            "H",
            "h",
            "I",
            "i",
            "J",
            "j",
            "K",
            "k",
            "L",
            "l",
            "M",
            "m",
            "N",
            "n",
            "O",
            "o",
            "P",
            "p",
            "Q",
            "q",
            "R",
            "r",
            "S",
            "s",
            "T",
            "t",
            "U",
            "u",
            "V",
            "v",
            "W",
            "w",
            "X",
            "x",
            "Y",
            "y",
            "Z",
            "z",
        ]
        for i in range(0, n):
            self.password += char_list[random.randint(0, 61)]
        return self.password

    def to_string(self):
        return (
            super().to_string()
            + f" lavora nel reparto {self.reparto} con un inquadramento_aziendale {self.inquadramento_aziendale}"
        )

    def calcola_stipendio(self):
        stipendio_base = {1: 1200, 2: 1500, 3: 2000, 4: 3000}
        coefficiente = {1: 1, 2: 1.1, 3: 1.2, 4: 1.3, 5: 1.4, 6: 1.5, 7: 2, 8: 2.5}
        stipendio = (
            stipendio_base[self.reparto] * coefficiente[self.inquadramento_aziendale]
        )
        print(f"Il tuo stipendio è: {stipendio}€")

    # metodo per modificare le ferie
    def settaFerie(self):
        flag = True
        while flag:
            print("Aggiungi orario ferie")
            print("Premi 1 per aggiornare le tue ferie 2 per uscire")
            scelta = input("Inserisci la tua risposta\n")
            if scelta == "1":
                print("Puoi richiedere fino a un massimo di 5 ore di ferie")
                nuove_ore = input("Inserisci le ore che vuoi richiedere\n")
                if controllo(1, 6, nuove_ore):
                    self.ore_Ferie = int(nuove_ore)
                    print("Ferie accettate")
                    flag = False
                else:
                    print("Inserire un comando valido")

            elif scelta == "2":
                print("Stai uscendo dal sistema...")
                flag = False

            else:
                print(
                    "Hai inserito un numero superiore a 5\n" "Inserisci numero valido\n"
                )

    # attributi: inquadramento_aziendale, reparto
    # metodo: calcolo_retribuzione, to_string (ereditato), scelta ferie


# -------------------------------------------- FUNZIONI --------------------------------------------------------
# login
def login():
    # Chiedi e controlla la pasword
    nome = input("Digita nome\n").strip()
    cognome = input("Digita cognome\n").strip()
    n_utente = controllo_esistenza_dipendente(nome, cognome, lista_dipendenti)
    if n_utente == "inesistente":
        pass  # da implementare
    else:
        if lista_dipendenti[n_utente].primo_ingresso == True:
            print("È il tuo primo ingresso, digita la tua nuova password")
            password_digitata = input()
            # Modifica la passsword
            lista_dipendenti[n_utente].password = password_digitata
            lista_dipendenti[n_utente].primo_ingresso = False

        else:
            if controllo_password_dipendente(lista_dipendenti, n_utente):
                # Esegui fino che l'utente non ha finito
                esci = False
                while not esci:
                    esci = menu_dipendente(n_utente)


def controllo_esistenza_dipendente(nome, cognome, lista_dipendenti):
    # Cicla
    for iteratore, dipendente in enumerate(lista_dipendenti):
        if dipendente.nome == nome and dipendente.cognome == cognome:
            print("L'utente esiste")
            return iteratore
    else:
        print("\nErrore: dipendente non registrato.\n")
        return "inesistente"


# Funzione per verificare che l'utente sia presente e conosca la pw corretta
def controllo_password_dipendente(lista_dipendenti, n_utente):
    print("Stai entranto come dipendente, digita la password")
    password_digitata = input()

    if password_digitata == lista_dipendenti[n_utente].password:
        print("\nPassword corretta.")  # inserire menù dipendente
        return True

    else:
        print("\nPassword errata.")
        return False


# Funzionalita per gestore: aggiungi dipendenti
def aggiungi_dipendente():
    print("Stai aggiungendo un nuovo dipendente")
    nome = str(input("Inserisci il nome: ")).strip()
    cognome = str(input("Inserisci il cognome: ")).strip()
    # Controlla se l'utente esiste giá
    if controllo_esistenza_dipendente(nome, cognome, lista_dipendenti) != "inesistente":
        print("L'utente inserito è giá presente")
        return None

    inquadramento_aziendale = input("Inserisci l'inquadramento aziendale: ").strip()
    reparto = input("Inserisci il reparto: ").strip()
    # aggiungi funzione controllo
    if controllo(1, 9, inquadramento_aziendale) and controllo(1, 5, reparto):
        dipendente = Dipendente(
            nome, cognome, int(inquadramento_aziendale), int(reparto)
        )
        lista_dipendenti.append(dipendente)
        print("Dipendente aggiunto con successo")
    else:
        print(
            "Errore,devi inserire un valore\n"
            "tra 0 e 8 per l'inquadramento aziendale\n "
            "e un valore tra 1 e 4 per il reparto\n"
        )


def modifica_dipendente():
    report()
    flag = False
    while not flag:
        indice_dipendente = input("Seleziona il dipendente da modificare: \n").strip()
        if controllo(0, len(lista_dipendenti), indice_dipendente):
            indice_dipendente_int = int(indice_dipendente)
            flag = True

    flag = False
    while not flag:
        print("Scegli l'opzione desiderata: ")
        print("1. Modifica nome")
        print("2. Modifica cognome")
        print("3. Modifica reparto")
        print("4. Modifica inquadramento aziendale")
        print("5. Esci")
        variabile = input().strip()

        if variabile == "1":
            nuovo_nome = str(input("Inserisci il nuovo nome: ")).strip()
            lista_dipendenti[indice_dipendente_int].nome = nuovo_nome

        elif variabile == "2":
            nuovo_cognome = str(input("Inserisci il nuovo cognome: ")).strip()
            lista_dipendenti[indice_dipendente_int].cognome = nuovo_cognome

        elif variabile == "3":
            flag2 = False
            while not flag2:
                nuovo_reparto = input("Inserisci il nuovo reparto\n").strip()
                if controllo(1, 5, nuovo_reparto):
                    flag2 = True
            lista_dipendenti[indice_dipendente_int].reparto = int(nuovo_reparto)

        elif variabile == "4":
            flag2 = False
            while not flag2:
                nuovo_inquadramento_aziendale = input(
                    "Inserisci il nuovo inquadramento aziendale\n"
                ).strip()
                if controllo(1, 9, nuovo_inquadramento_aziendale):
                    flag2 = True
            lista_dipendenti[indice_dipendente_int].inquadramento_aziendale = int(
                nuovo_inquadramento_aziendale
            )

        elif variabile == "5":
            flag = True
            continue

        else:
            print("Scegliere un comando valido")
            continue

        print("Modifica avvenuta con successo")
        print(lista_dipendenti[indice_dipendente_int].to_string())


def controllo(a, b, elemento):
    valori_accettabili = [str(iteratore) for iteratore in range(a, b)]
    if elemento in valori_accettabili:
        return True
    else:
        return False


# Funzionalita per gestore: rimuovi dipendenti
def rimuovi_dipendente():
    report()
    indice_dipendente = int(
        input("Seleziona il dipendente che hai deciso di rimuovere\n").strip()
    )
    lista_dipendenti.pop(indice_dipendente)
    print("Dipendente rimosso")


# Funzionalita per gestore: stampa il report
def report():
    if lista_dipendenti == []:
        print("Non ci sono dipendenti nella lista")
    else:
        for iteratore, elemento in enumerate(lista_dipendenti):
            print(f"{iteratore}. {elemento.to_string()}")


# MENU scelte dipendente: stampa retribuzione o gestisci ferie
def menu_dipendente(n_utente):
    print("Scegli l'opzione desiderata: ")
    print("1. Visualizza la propria retribuzione")
    print("2. Aggiungi giorni ferie")
    print("3. Esci")

    variabile = input().strip()

    if variabile == "1":
        lista_dipendenti[n_utente].calcolo_stipendio()

    elif variabile == "2":
        lista_dipendenti[n_utente].settaFerie()

    elif variabile == "3":
        return "esci"

    else:
        print("Scegliere un comando valido")


# MENU scelta gestore: gestisci lista dipendenti (CRUD) o stampa report
def menu_gestore():
    print("Scegli l'opzione desiderata: ")
    print("1. Aggiungi dipendenti")
    print("2. Modificare un dipendente")
    print("3. Rimuovi dipendenti")
    print("4. Report")
    print("5. Esci")

    variabile = input().strip()

    if variabile == "1":
        aggiungi_dipendente()

    elif variabile == "2":
        modifica_dipendente()

    elif variabile == "3":
        rimuovi_dipendente()

    elif variabile == "4":
        report()

    elif variabile == "5":
        return "esci"  # True

    else:
        print("Scegliere un comando valido")


# -------------------------------------------- BLOCCO CODICE PRINCIPALE --------------------------------------------------------


# Inizio codice
dip1 = Dipendente("Mario", "Rossi", 1, 2)
dip2 = Dipendente("Luigi", "Bianchi", 3, 4)
dip1.genera_password(4)
dip2.genera_password(4)
lista_dipendenti.append(dip1)
lista_dipendenti.append(dip2)
dip1.calcola_stipendio()


# Inizia I/O: ripeti richiesta scelta per output errati, altrimenti esci
# flag = False
flag = True
while not flag:
    print("Scegli il tipo di account: ")
    print("1. Account gestore")
    print("2. Account dipendente")
    print("3. Esci")

    variabile = input().strip()

    if variabile == "1":
        # Chiedi e controlla la pasword
        print("Stai entranto come gestore, digita la password")
        password_digitata = input()
        if password_digitata != admin_password:
            print("Password errata! Chiusura del programma in corso...")
        else:
            # Esegui azioni fino che l'utente non ha finito
            esci = False
            while not esci:
                esci = menu_gestore()

    elif variabile == "2":
        login()
    elif variabile == "3":
        print("esci")
        flag = True

    else:
        print("Scegliere un comando valido")

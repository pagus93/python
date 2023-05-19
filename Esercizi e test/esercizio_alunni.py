
# CREARE UNA CLASSE LISTAALLUNNI, che dovrà essere sempre valorizzata appena si accede al primo menu,
# Un primo menu con entra o esci, se esci si chiude tutto, se entri devi darmi X nomi obbligatori e X corrispettivi voti agli studenti,
# L'esericizio sarà creare un sistema che permetta di andare a scegliere un singolo utente e di modificare e aggiungere i suoi voti

alunni = []
materie = []
voti = []

class Alunno:
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome
    def aggiungi(self):
        for i in range(0,len(alunni)):
            if alunni[i].nome == self.nome and alunni[i].cognome == self.cognome:
                break
        else:
            alunni.append(self)

class Materia(Alunno):
    def __init__(self,nome,cognome,materia):
        super().__init__(nome,cognome)
        self.materia = materia
    def aggiungi(self):
        for j in range(0,len(materie)):
            if materie[j].nome == self.nome and materie[j].cognome == self.cognome and materie[j].materia == self.materia:
                break
        else:
            materie.append(self)

class Voto(Materia):
    def __init__(self,nome,cognome,materia,voto):
        super().__init__(nome,cognome,materia)
        self.voto = voto
    def aggiungi(self):
        voti.append(self)

flag1 = False
while not flag1:
    scelta = int(input("\nBenvenuto.\nPremere 1 per registrare nuovi voti.\nPremere 2 per visualizzare o modificare le schede alunni.\nPremere 0 per uscire.\n"))

    if scelta == 0:
        flag1 = True

    elif scelta == 1:
        flag2 = False
        while not flag2:
            n = int(input("\nInserire il numero di voti da registrare (inserire '0' per tornare indietro): "))
            if n == 0:
                flag2 = True
            else:
                for m in range(0,n):
                    nome = input("\nInserire il nome dell'alunno: ")
                    cognome = input("Inserire il cognome dell'alunno: ")
                    materia = input("Inserire la materia valutata: ")
                    voto = input("Inserire il voto: ")

                    Alunno(nome,cognome).aggiungi()
                    Materia(nome,cognome,materia).aggiungi()
                    Voto(nome,cognome,materia,voto).aggiungi()
    
    elif scelta == 2:
        nome = input("\nInserire il nome dell'alunno: ")
        cognome = input("Inserire il cognome dell'alunno: ")
        for i in range(0,len(alunni)):
            if alunni[i].nome == nome and alunni[i].cognome == cognome:
                print(f"\nI voti dell'alunno {nome} {cognome} suddivisi per materia sono:")
                for j in range(0,len(materie)):
                    if materie[j].nome == alunni[i].nome and materie[j].cognome == alunni[i].cognome:
                        print(f"\n{materie[j].materia}:")
                        for k in range(0,len(voti)):
                            if voti[k].nome == materie[j].nome and voti[k].cognome == materie[j].cognome and voti[k].materia == materie[j].materia:
                                print(voti[k].voto)
            break
        else:
            print("Errore: alunno non trovato.")
        

    else:
        print("Errore: input non riconosciuto.\n")



#
#print()
#for i in range(0,len(alunni)):
#    print(f"nome: {alunni[i].nome}, cognome: {alunni[i].cognome}")
#print()
#for j in range(0,len(materie)):
#    print(f"nome: {materie[j].nome}, cognome: {materie[j].cognome}, materia: {materie[j].materia}")
#print()
#for k in range(0,len(voti)):
#    print(f"nome: {voti[k].nome}, cognome: {voti[k].cognome}, materia: {voti[k].materia}, voto: {voti[k].voto}")
#print()
#

        
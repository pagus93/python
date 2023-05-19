
class Persona:
    tipo = "umano"

    def __init__(self, nome, eta):
        self.nome =  nome
        self.eta = eta
    
    def masterD(self):
        print(f"ciao, sono {self.nome} di tipo {self.tipo}")

x = Persona("Mirko", 99)
x.masterD()

class Allievo(Persona):

    def __init__(self, nome, eta, grado):
        super().__init__(nome, eta)
        self.grado = grado
    
    tipo = "gatto"

    def masterD(self):
        print(f"ciao, sono {self.nome} di grado {self.grado}")

y = Allievo("Marius", 23, "Terzo dan")
y.masterD()

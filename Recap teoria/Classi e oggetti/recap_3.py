
class Persona:
    age = 0
    name = ""

    # metodo costruttore
    def __init__(self, name, age): # self è un placeholder
        self.name = name
        self.age = age

pippo = Persona("Pippo", 10)
mirko = Persona("Antonello", 34)


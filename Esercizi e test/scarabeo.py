
import random

class Dado:
    facce = 1
    def lancia(self):
        n = random.randint(1,self.facce)
        return n

char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

dado = Dado()
dado.facce = 26
parola = ""

for i in range(0,4):
    n = dado.lancia()
    parola += char_list[n]

print(parola)

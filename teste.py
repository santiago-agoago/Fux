lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
import random

def gerar_nota():
    return random.randint(0, 10)

nota = gerar_nota()
print(nota)
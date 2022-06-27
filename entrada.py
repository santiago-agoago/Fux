from dicionario import *

class CF:
    def __init__(self, modo, voz):
        self.modo = modo
        self.voz = voz
class RES:
    def __init__(self, reg, voz):
        self.reg = reg
        self.notas = []
        self.voz = voz
    def add(self, nota):
        self.notas.append(nota)
    def clear(self):
        self.notas = []

def cf_auto():
    global cf
    global cp
    print("\nQual o cantus firmus?\n1. Dórico\n2. Frígio\n3. Lídio\n4. Mixolídio\n5. Eólio\n6. Jônico")
    entrada1 = int(input("> "))
    print("\nGerar melodia inferior ou superior?\n1. Superior\n2. Inferior")
    entrada2 = int(input("> "))
    if entrada1 == 1:
        cf = CF(dorico, a)
        if entrada2 == 1:
            cp = RES(2, s)
        if entrada2 == 2:
            cp = RES(1, t)
    if entrada1 == 2:
        cf = CF(frigio, a)
        if entrada2 == 1:
            cp = RES(2, s)
        if entrada2 == 2:
            cp = RES(1, t)
    if entrada1 == 3:
        cf = CF(lidio, t)
        if entrada2 == 1:
            cp = RES(2, a)
        if entrada2 == 2:
            cp = RES(1, b)
    if entrada1 == 4:
        cf = CF(mixo, a)
        if entrada2 == 1:
            cp = RES(2, s)
        if entrada2 == 2:
            cp = RES(1, t)
    if entrada1 == 5:
        cf = CF(eolio, a)
        if entrada2 == 1:
            cp = RES(2, s)
        if entrada2 == 2:
            cp = RES(1, t)
    if entrada1 == 6:
        cf = CF(jonico, a)
        if entrada2 == 1:
            cp = RES(2, s)
        if entrada2 == 2:
            cp = RES(1, t)

    return cf, cp
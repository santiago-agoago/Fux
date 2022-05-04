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
    global contra
    print("\nQual o cantus firmus?\n1. Dórico\n2. Frígio\n3. Lídio\n4. Mixolídio\n5. Eólio\n6. Jônico")
    entrada1 = int(input("> "))
    print("\nGerar melodia inferior ou superior?\n1. Superior\n2. Inferior")
    entrada2 = int(input("> "))
    if entrada1 == 1:
        cf = CF(dorico, "alto")
        if entrada2 == 1:
            contra = RES(2, "soprano")
        if entrada2 == 2:
            contra = RES(1, "tenor")
    if entrada1 == 2:
        cf = CF(frigio,"alto")
        if entrada2 == 1:
            contra = RES(2, "soprano")
        if entrada2 == 2:
            contra = RES(1, "tenor")
    if entrada1 == 3:
        cf = CF(lidio, "tenor")
        if entrada2 == 1:
            contra = RES(2, "alto")
        if entrada2 == 2:
            contra = RES(1, "bass")
    if entrada1 == 4:
        cf = CF(mixo, "alto")
        if entrada2 == 1:
            contra = RES(2, "soprano")
        if entrada2 == 2:
            contra = RES(1, "tenor")
    if entrada1 == 5:
        cf = CF(eolio, "alto")
        if entrada2 == 1:
            contra = RES(2, "soprano")
        if entrada2 == 2:
            contra = RES(1, "tenor")
    if entrada1 == 6:
        cf = CF(jonico, "alto")
        if entrada2 == 1:
            contra = RES(2, "soprano")
        if entrada2 == 2:
            contra = RES(1, "tenor")

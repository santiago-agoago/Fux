import random
from dicionario import *


class CF:
    def __init__(self, modo, naipe):
        self.modo = modo
        self.naipe = naipe
    def clave(self):
        if self.naipe == 1:
            return "bass"
        else:
            return "alto"
class RES:
    def __init__(self, naipe):
        self.naipe = naipe
        self.notas = []
    def add(self, nota):
        self.notas.append(nota)
    def clear(self):
        self.notas = []

def cf_auto():
    global cf
    global contra
    print("\nQual o cantus firmus?\n1. Jônico\n2. Dórico\n3. Frígio\n4. Lídio\n5. Mixolídio\n6. Eólio")
    entrada = int(input("> "))
    print("\nGerar melodia inferior ou superior?\n1. Superior\n2. Inferior")
    if entrada == 1:
        cf = CF(jonico, int(input("> ")))
    if entrada == 2:
        cf = CF(dorico, int(input("> ")))
    if entrada == 3:
        cf = CF(frigio, int(input("> ")))
    if entrada == 4:
        cf = CF(lidio, int(input("> ")))
    if entrada == 5:
        cf = CF(mixo, int(input("> ")))
    if entrada == 6:
        cf = CF(eolio, int(input("> ")))
    print("\nPara que naipe?\nS A T B")
    entrada2 = str(input("> ").lower())
    if entrada2 == "s":
        contra = RES(s)
    if entrada2 == "a":
        contra = RES(a)
    if entrada2 == "t":
        contra = RES(t)
    if entrada2 == "b":
        contra = RES(b)
#print
def print_prim_esp(cf, contra):
    if cf.naipe == 1:
        print("\n\\version \"2.22.2\"\n\\language \"portugues\" \n<<\n\\new Staff {\n\\clef ", contra.naipe["clave"])
        for i in range(len(contra.notas)):
            print(midi_ly[contra.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n\\new Staff \with {instrumentName = \"CF\"}\n{\n\\clef bass")
        for i in range(len(cf.modo)):
            print(midi_ly[cf.modo[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n>>")
    else:
        print("\n\\version \"2.22.2\"\n\\language \"portugues\" \n<<\n\\new Staff \with {instrumentName = \"CF\"}\n{\n\\clef alto")
        for i in range(len(cf.modo)):
            print(midi_ly[cf.modo[i] + 12], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n\\new Staff {\n\\clef ", contra.naipe["clave"])
        for i in range(len(contra.notas)):
            print(midi_ly[contra.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n>>")
#quantizador
def gerar_nota(contra):
    nota2 = random.randint(contra.naipe["mi"], contra.naipe["ma"])
    if nota2 not in naturais:
        return nota2 + 1
    else:
        return nota2
#intervalo
def int_har(nota1, nota2):
    return abs(nota1 - nota2)
def int_mel(nota, notal):
    return notal - nota

#filtros
def filt_tess(nota, naipe):
    if nota > naipe["ma"] or nota < naipe["mi"]:
        return True
def filt_diss(nota1, nota2):
    if abs(nota1 - nota2) not in int_cons:
        return True
def filt_pll(i, cf, res, nota):
    if int_har(cf[i - 1], res[i - 1]) in conper:
        if int_har(cf[i], nota) in conper:
            return True

        if int_mel(res[i - 1], nota) >= 1 and int_mel(cf[i - 1], cf[i]) >= 1:
            return True
        if int_mel(res[i - 1], nota) <= -1 and int_mel(cf[i - 1], cf[i]) <=-1:
            return True
def filt_meldis(i, res, nota):
    if int_mel(res[i -1], nota) in int_meldis:
        return True
    if int_har(res[i - 1], nota) > 12:
        return True



def filt_rep(i, res, nota):
    if nota == res[i - 1]:
        return True


#gera primeira espécie
def main(cf, contra):
    global it
    it = 1
    completou = False
    abortar = False
    while completou == False and abortar == False:
        contra.clear()
        j = 0
        #primeira nota
        while len(contra.notas) == 0:
            it += 1
            j += 1
            if cf.naipe == 1:
                nota2 = random.randint(0, 1) * 12 + cf.modo[0]
                if not filt_tess(nota2, contra.naipe):
                    contra.add(nota2)
            else:
                nota2 = random.randint(-1, 0) * 12 + cf.modo[0]
                if not filt_tess(nota2, contra.naipe):
                    contra.add(nota2)
            if j == 100:
                for k in range(2):
                    if cf.naipe == 1:
                        nota2 = k
                        if not filt_tess(nota2, contra.naipe):
                            contra.add(nota2)
                    else:
                        nota2 = k
                        if not filt_tess(nota2, contra.naipe):
                            contra.add(nota2)
                if len(contra.notas) == 0:
                    print("Naipe incompatível")
                    abortar = True
                    break
        for i in range(1, len(cf.modo)):
            #última nota
            if len(contra.notas) == len(cf.modo) - 1:
                if not filt_pll(i, cf.modo, contra.notas, contra.notas[0]):
                    contra.add(contra.notas[0])
                    completou = True
                    print("\n")
                    print(f"tentativas: {it}")
                    break

            else:
                nota2 = gerar_nota(contra)
                #filtros
                if filt_diss(cf.modo[i], nota2) \
                or filt_pll(i, cf.modo, contra.notas, nota2)\
                or filt_rep(i, contra.notas, nota2)\
                or filt_meldis(i, contra.notas, nota2):
                    it += 1
                    break

                else:
                    contra.add(nota2)
        if it >= 5000000:
            print("\nExcedeu limite de iterações")
            abortar = True
            break

cf_auto()
print("\n", cf.modo, cf.naipe, contra.naipe)
main(cf, contra)
print(f"cantus firmus:{cf.modo}\nresolução:    {contra.notas}\niterações:    {it}")
print_prim_esp(cf, contra)
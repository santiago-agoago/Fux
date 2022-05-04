import random
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

#print
def print_prim_esp(cf, cp):
    if cp.reg == 2:
        print("\n\\version \"2.22.2\"\n\\language \"portugues\" \n<<\n\\new Staff {\n\\clef ", cp.voz["clave"])
        for i in range(len(cp.notas)):
            print(midi_ly[cp.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n\\new Staff \with {instrumentName = \"CF\"}\n{\n\\clef", cf.voz["clave"])
        for i in range(len(cf.modo)):
            print(midi_ly[cf.modo[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n>>")
    else:
        print("\n\\version \"2.22.2\"\n\\language \"portugues\" \n<<\n\\new Staff \with {instrumentName = \"CF\"}\n{\n\\clef", cf.voz["clave"])
        for i in range(len(cf.modo)):
            print(midi_ly[cf.modo[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n\\new Staff {\n\\clef ", cp.voz["clave"])
        for i in range(len(cp.notas)):
            print(midi_ly[cp.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n>>")
#quantizador
def gerar_nota(cp):
    nota2 = random.randint(cp.voz["mi"], cp.voz["ma"])
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
    #regras melódicas
def filt_tess(nota, voz):
    if nota > voz["ma"] or nota < voz["mi"]:
        return True
def filt_rep(i, res, nota):
    if i > 1 and nota == res[i - 1] and nota == res[i - 2]:
        return True
def filt_meldis(i, res, nota):
    if int_mel(res[i -1], nota) in int_meldis:
        return True
    if int_har(res[i - 1], nota) > 12:
        return True
    #regras harmônicas
def filt_diss(nota1, nota2):
    if abs(nota1 - nota2) not in int_cons:
        return True
    #regras combinadas (Hiller, 1959)
def filt_pll(i, cf, res, nota):
    if int_har(cf[i], nota) in conper:
        if int_mel(res[i - 1], nota) >= 1 and int_mel(cf[i - 1], cf[i]) >= 1:
            return True
        if int_mel(res[i - 1], nota) <= 1 and int_mel(cf[i - 1], cf[i]) <= -1:
            return True


#cadência primeira espécie
def cad_prim(cf, cp, i):
# cadência tipo 1
    if cf.modo == dorico or cf.modo == eolio:
        if cp.reg == 2:
            nota2 = cf.modo[len(cf.modo) - 1] + 12
            if not filt_pll(i, cf.modo, cp.notas, nota2) or filt_meldis(i, cp.notas, nota2) or filt_rep(i, cp.notas, nota2):
                cp.add(nota2)
        else:
            nota2 = cf.modo[len(cf.modo) - 1]
            if not filt_pll(i, cf.modo, cp.notas, nota2) or filt_meldis(i, cp.notas, nota2) or filt_rep(i, cp.notas, nota2):
                cp.add(nota2)

# cadência tipo 1 ou tipo 2
    elif cf.modo == frigio:
        if cp.reg == 2:
            nota2 = cf.modo[len(cf.modo) - 1] + 12
            if not filt_pll(i, cf.modo, cp.notas, nota2) or filt_meldis(i, cp.notas, nota2) or filt_rep(i, cp.notas, nota2):
                cp.add(nota2)
        else:
            np = [cf.modo[len(cf.modo) - 1] - 4, cf.modo[len(cf.modo) - 1]]
            random.shuffle(np)
            while len(cp.notas) < len(cf.modo) - 2:
                for i in range(2):
                    nota2 = np[i]
                    if not filt_pll(i, cf.modo, cp.notas, nota2) or filt_meldis(i, cp.notas, nota2) or filt_rep(i, cp.notas, nota2):
                        cp.add(nota2)
                    if i > 2:
                        break
    else:
        if cp.reg == 2:
            nota2 = cf.modo[len(cf.modo) - 1] + 12
            if not filt_pll(i, cf.modo, cp.notas, nota2) or filt_meldis(i, cp.notas, nota2) or filt_rep(i, cp.notas, nota2):
                cp.add(nota2)
        else:
            np = [cf.modo[len(cf.modo) - 1] - 3, cf.modo[len(cf.modo) - 1]]
            random.shuffle(np)
            while len(cp.notas) < len(cf.modo) - 2:
                for i in range(2):
                    nota2 = np[i]
                    if not filt_pll(i, cf.modo, cp.notas, nota2) or filt_meldis(i, cp.notas, nota2) or filt_rep(i, cp.notas, nota2):
                        cp.add(nota2)
                    if i > 2:
                        break

# penúltima e última nota
    if cp.reg == 2:
        nota2 = cf.modo[len(cf.modo) - 2] + 9
        cp.add(nota2)
        cp.add(cf.modo[len(cf.modo) - 1] + 12)
        return True
    else:
        nota2 = cf.modo[len(cf.modo) - 2] - 3
        cp.add(nota2)
        cp.add(cf.modo[len(cf.modo) - 1])
        return True

#gera primeira espécie
def main(cf, cp):
    global it
    it = 1
    completou = False
    abortar = False
    while completou == False and abortar == False:
        cp.clear()
        j = 0
        #primeira nota
        while len(cp.notas) == 0:
            it += 1
            j += 1

            if cp.reg == 1:
                random.shuffle(prim_nota_sup)
                for i in range(3):
                    nota2 = (cf.modo[0] + prim_nota_sup[i])
                    if not filt_tess(nota2, cp.voz):
                        cp.add(nota2)
                        break
            else:
                random.shuffle(prim_nota_inf)
                for i in range(2):
                    nota2 = cf.modo[0] + prim_nota_inf[i]
                    if not filt_tess(nota2, cp.voz):
                        cp.add(nota2)
                        break
            if len(cp.notas) == 0:
                print("Voz incompatível")
                abortar = True
                break
        #principal
        for i in range(1, len(cf.modo)):
            #CADENCIA
            if i == len(cf.modo) - 3:
                #sub-rotina de cadência
                if cad_prim(cf, cp, i):
                    completou = True
                    print("\n")
                    print(f"tentativas: {it}")
                    break

            else:
                nota2 = gerar_nota(cp)
                #filtros
                if filt_diss(cf.modo[i], nota2) \
                or filt_pll(i, cf.modo, cp.notas, nota2)\
                or filt_rep(i, cp.notas, nota2)\
                or filt_meldis(i, cp.notas, nota2):
                    it += 1
                    break

                else:
                    cp.add(nota2)
        if it >= 5000000:
            print("\nExcedeu limite de iterações")
            abortar = True
            break

cf_auto()
print("\n", cf.modo, cf.voz, "\n", cp.reg, cp.voz)
main(cf, cp)
print(f"cantus firmus:{cf.modo}\nresolução:    {cp.notas}\niterações:    {it}")
print_prim_esp(cf, cp)
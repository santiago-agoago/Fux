import random
import statistics
#testando git2
#teste3

midi_ly = {
    36 : "do,",
    37 : "dos,",
    38 : "re,",
    39 : "res,",
    40 : "mi,",
    41 : "fa,",
    42 :  "fas,",
    43 : "sol,",
    44 : "sols,",
    45 : "la,",
    46 : "las,",
    47 : "si,",
    48 : "do",
    49 : "dos",
    50 : "re",
    51 : "res",
    52 : "mi",
    53 : "fa",
    54 : "fas",
    55 : "sol",
    56 : "sols",
    57 : "la",
    58 : "las",
    59 : "si",
    60 : "do'",
    61 : "dos'",
    62 : "re'",
    63 : "res'",
    64 : "mi'",
    65 : "fa'",
    66 : "fas'",
    67 : "sol'",
    68 : "sols'",
    69 : "la'",
    70 : "las'",
    71 : "si'",
    72 : "do''",
    73 : "dos''",
    74 : "re''",
    75 : "res''",
    76 : "mi''",
    77 : "fa''",
    78 : "fas''",
    79 : "sol''",
    80 : "sols''",
    81 : "la''",
    82 : "las''",
    83 : "si''",
    84 : "do'''",
}
jonico = [48, 52, 53, 55, 52, 57, 55, 52, 53, 52, 50, 48]
dorico = [50, 53, 52, 50, 55, 53, 57, 55, 53, 52, 50]
frigio = [52, 48, 50, 48, 45, 57, 55, 52, 53, 52]
lidio = [53, 55, 57, 53, 50, 52, 53, 60, 57, 53, 55, 53]
mixo = [43, 48, 47, 43, 48, 52, 50, 55, 52, 48, 50, 47, 45, 43]
eolio = [57, 60, 59, 62, 60, 64, 65, 64, 62, 60, 59, 57]
cf = []
naturais = [36, 38, 40, 41, 43, 45, 47, 48,	50,	52,	53,	55,	57,	59, 60,	62,	64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84]
int_cons = [3, 4, 7, 8, 9, 12, 15, 16, 19, 20, 21]
#naipes
s = {"mi" : 60, "ma" : 79, "clave" : "soprano"}
a = {"mi" : 55, "ma" : 74, "clave" : "alto"}
t = {"mi" : 48, "ma" : 67, "clave" : "tenor"}
b = {"mi" : 40, "ma" : 60, "clave" : "bass"}

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
    def notas(self):
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
def oitava(modo):
    for i in range(len(modo)):
        modo[i] -= 12
    print(modo)

def print_prim_esp(cf, res):
    if cf.naipe == 1:
        print("\n\\version \"2.22.2\"\n\\language \"portugues\" \n<<\n\\new Staff {\n\\clef ", res.naipe["clave"])
        for i in range(len(res.notas)):
            print(midi_ly[res.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n\\new Staff \with {instrumentName = \"CF\"}\n{\n\\clef bass")
        for i in range(len(cf.modo)):
            print(midi_ly[cf.modo[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n>>\n")
    else:
        print("\n\\version \"2.22.2\"\n\\language \"portugues\" \n<<\n\\new Staff \with {instrumentName = \"CF\"}\n{\n\\clef alto")
        for i in range(len(cf.modo)):
            print(midi_ly[cf.modo[i] + 12], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n\\new Staff {\n\\clef ", res.naipe["clave"])
        for i in range(len(res.notas)):
            print(midi_ly[res.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n>>\n")


#quantizador
def quant(nota):
    if nota not in naturais:
        return nota + 1
    else:
        return nota

#verificações
def verif_cons(nota1, nota2):
    if abs(nota1 - nota2) in int_cons:
        return True
    else:
        return False
def verif_tess(nota, naipe):
    if nota > naipe["ma"] or nota < naipe["mi"]:
        return False
    else:
        return True

#gera primeira espécie
def prim_esp(cf, contra):
    global res
    global it
    it = 1
    res = []
    completou = False
    while completou == False:
        res = []

        #primeira nota
        if cf.naipe == 1:
            nota2 = random.randint(0, 1) * 12 + cf.modo[0]
            if verif_tess(nota2, contra.naipe):
                res.append(nota2)
        else:
            nota2 = random.randint(-1, 0) * 12 + cf.modo[0]
            if verif_tess(nota2, contra.naipe):
                res.append(nota2)

        for i in range(len(cf.modo)):
            i += 1
            #última nota
            if i == len(cf.modo) - 1:
                    res.append(res[0])
                    completou = True
                    print("\n")
                    break

            else:
                nota2 = random.randint(contra.naipe["mi"], contra.naipe["ma"])
                nota2 = quant(nota2)
                if verif_cons(cf.modo[i], nota2):
                    res.append(nota2)

                #nova tentativa
                else:
                    it += 1
                    print(".", end="")
                    break
        if it >= 100000:
            print("\nExcedeu limite de iterações")
            break
    print("resolução:     ", res)
    print("cantus firmus: ", cf.modo)

    contra.notas = res

cf_auto()
print("\n", cf.modo, cf.naipe, contra.naipe,"\n")
prim_esp(cf, contra)
print_prim_esp(cf, contra)

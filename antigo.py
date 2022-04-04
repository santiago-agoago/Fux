import random
import statistics

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
jonico = [60, 64, 65, 67, 64, 69, 67, 64, 65, 64, 62, 60]
dorico = [62, 65, 64, 62, 67, 65, 69, 67, 65, 64, 62]
frigio = [64, 60, 62, 60, 57, 69, 67, 64, 65, 64]
lidio = [65, 67, 69, 65, 62, 64, 65, 72, 69, 65, 67, 65]
mixo = [43, 48, 47, 43, 48, 52, 50, 55, 52, 48, 50, 47, 45, 43]
eolio = [57, 60, 59, 62, 60, 64, 65, 64, 62, 60, 59, 57]
cf = []
naturais = [36, 38, 40, 41, 43, 45, 47, 48,	50,	52,	53,	55,	57,	59, 60,	62,	64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84]
int_cons = [3, 4, 7, 8, 9, 12, 15, 16, 19, 20, 21, 24]

#entrada do cf
def cf_manual():
    cf = cf.split()
    cf = [int(i) for i in cf]
def cf_auto():
    global cf
    print("Qual o cantus firmus?\n1. jônico\n2. dórico\n3. frígio\n4. lídio\n5. mixolídio\n6. eólio")
    modo = int(input("> "))
    if modo == 1:
        cf = jonico
    if modo == 2:
        cf = dorico
    if modo == 3:
        cf = frigio
    if modo == 4:
        cf = lidio
    if modo == 5:
        cf = mixo
    if modo == 6:
        cf = eolio
#quantizador
def quant(nota):
    if nota not in naturais:
        return nota + 1
    else:
        return nota
#verifica consonâncias
def verif_cons(nota, cf):
    if abs(cf - nota) in int_cons:
        return True
    else:
        return False
#gera primeira espécie
def prim_esp(cf):
    global melo_cons
    global it
    it = 1
    melo_cons = []
    completou = False
    while completou == False:
        i = 0
        melo_cons = []
        for i in range(len(cf)):
            nota = random.randint(cf[i], 84)
            nota = quant(nota)
            if verif_cons(nota, cf[i]):
                melo_cons.append(nota)
                if len(melo_cons) == len(cf):
                    completou = True
                    print("\n")
            else:
                it += 1
                print(".", end = "")
                break
    print(cf)
    print(melo_cons)

#prints
def print_ly(cf):
    print("\\version \"2.22.2\"\n\\language \"portugues\" \n {\n\\clef alto")
    for i in range(len(cf)):
        print(midi_ly[cf[i]], "1", sep = "", end = " ")
        if i == len(cf) - 1:
            print("\n}")
def print_prim_esp(cf, melo_cons):
    print("\n\\version \"2.22.2\"\n\\language \"portugues\" \n<<\n\\new Staff {")
    for i in range(len(melo_cons)):
        print(midi_ly[melo_cons[i]], "1", sep="", end=" ")
        if i == len(cf) - 1:
            print("\n}\n\\new Staff \with {instrumentName = \"CF\"}\n{\n\\clef bass")
    for i in range(len(cf)):
        print(midi_ly[cf[i]], "1", sep="", end=" ")
        if i == len(cf) - 1:
            print("\n}\n>>\n")

#testes
def it_med(cf, amostra):
    media = []
    for i in range(amostra):
        global it
        it = 1
        melo_cons = []
        completou = False
        while completou == False:
            i = 0
            melo_cons = []
            for i in range(len(cf)):
                nota = random.randint(cf[i], 84)
                nota = quant(nota)
                if verif_cons(nota, cf[i]):
                    melo_cons.append(nota)
                    if len(melo_cons) == len(cf):
                        completou = True
                else:
                    it += 1
                    break

        media.append(it)
    print(statistics.mean(media))
def analise(amostra):
    print("jonico:")
    it_med(jonico, amostra)
    print("dorico:")
    it_med(dorico, amostra)
    print("frigio:")
    it_med(frigio, amostra)
    print("lidio:")
    it_med(lidio, amostra)
    print("mixolidio:")
    it_med(mixo, amostra)
    print("eolio:")
    it_med(eolio, amostra)

#realizar primeira espécie
while True:
    cf_auto()
    prim_esp(cf)
    print_prim_esp(cf, melo_cons)
    print(it)
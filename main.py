import random
from aritmetica import *
from saida import *

#quantizador
def gerar_nota(cp):
    nota2 = random.randint(cp.voz["mi"], cp.voz["ma"])
    if nota2 not in naturais:
        return nota2 + 1
    else:
        return nota2

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
            for i in range(2):
                nota2 = np[i]
                if not filt_pll(i, cf.modo, cp.notas, nota2) or filt_meldis(i, cp.notas, nota2) or filt_rep(i, cp.notas, nota2):
                    cp.add(nota2)
                    break

    else:
        if cp.reg == 2:
            nota2 = cf.modo[len(cf.modo) - 1] + 12
            if not filt_pll(i, cf.modo, cp.notas, nota2) or filt_meldis(i, cp.notas, nota2) or filt_rep(i, cp.notas, nota2):
                cp.add(nota2)
        else:
            np = [cf.modo[len(cf.modo) - 1] - 3, cf.modo[len(cf.modo) - 1]]
            random.shuffle(np)
            for i in range(2):
                nota2 = np[i]
                if not filt_pll(i, cf.modo, cp.notas, nota2) or filt_meldis(i, cp.notas, nota2) or filt_rep(i, cp.notas, nota2):
                    cp.add(nota2)
                    break

# penúltima e última nota
    if len(cp.notas) == len(cf.modo) - 2:
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
    else:
        return False

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

            if cp.reg == 2:
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
            if len(cp.notas) == len(cf.modo) - 3:
                #sub-rotina de cadência
                if cad_prim(cf, cp, i):
                    completou = True
                    print(f"tentativas: {it}")
                    break
                else:
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

#cp, cf = cf_auto()
#print("\n", cf.modo, cf.voz, "\n", cp.reg, cp.voz)
#main(cf, cp)
#print(f"cantus firmus:{cf.modo}\nresolução:    {cp.notas}\niterações:    {it}")
#print_prim_esp(cf, cp)
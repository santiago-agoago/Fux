from aritmetica import *
import random

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
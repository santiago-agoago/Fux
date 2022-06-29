from aritmetica import *
import random
def filtros(i, cf, cp, nota):
    if filt_pll(i, cf.modo, cp.notas, nota) \
            or filt_meldis(i, cp.notas, nota) \
            or filt_rep(i, cp.notas, nota) \
            or filt_saltos(i, cp.notas, nota)\
            or filt_ext(cp.notas, nota):
        return True

def final_tipo1(i, cf, cp, ante):
    if cp.reg == 2:
        cp.add(ante)
        cp.add(cf.modo[len(cf.modo) - 2] + 9)
        cp.add(ante)
    else:
        if int_har(ante, cp.notas[-1]) > 6 and int_har(ante - 12, cp.notas[-1]) < 6:
            if not filtros(i, cf, cp, ante):
                cp.add(ante - 12)
                cp.add(cf.modo[len(cf.modo) - 2] - 15)
                cp.add(ante - 12)
            else:
                cp.add(ante)
                cp.add(cf.modo[len(cf.modo) - 2] - 3)
                cp.add(ante)

        else:
            cp.add(ante)
            cp.add(cf.modo[len(cf.modo) - 2] - 3)
            cp.add(ante)


def final_tipo2(i, cf, cp, ante):
    if cp.reg == 2:
        cp.add(ante)
        cp.add(cf.modo[len(cf.modo) - 2] + 9)
        cp.add(cf.modo[len(cf.modo) - 1] + 12)
    else:
        if int_har(ante, cp.notas[-1]) > 6 and int_har(ante - 12, cp.notas[-1]) < 6:
            if not filtros(i, cf, cp, ante):
                cp.add(ante - 12)
                cp.add(cf.modo[len(cf.modo) - 2] - 15)
                cp.add(cf.modo[len(cf.modo) - 1] - 12)
            else:
                cp.add(ante)
                cp.add(cf.modo[len(cf.modo) - 2] - 3)
                cp.add(cf.modo[len(cf.modo) - 1])

        else:
            cp.add(ante)
            cp.add(cf.modo[len(cf.modo) - 2] - 3)
            cp.add(cf.modo[len(cf.modo) - 1])




#cadência primeira espécie
def cad_prim(cf, cp, i):
# antepenúltima nota
# cadência tipo 1
    if cf.modo == dorico or cf.modo == eolio:
        if cp.reg == 2:
            nota2 = cf.modo[len(cf.modo) - 1] + 12
            if not filtros(i, cf, cp, nota2):
                final_tipo1(i, cf, cp, nota2)
                return True

        else:
            # IF
            nota2 = cf.modo[len(cf.modo) - 1]
            if not filtros(i, cf, cp, nota2):
                final_tipo1(i, cf, cp, nota2)
                return True

# cadência tipo 1 ou tipo 2
    elif cf.modo == frigio:
        #tipo 1
        if cp.reg == 2:
            nota2 = cf.modo[len(cf.modo) - 1] + 12
            if not filtros(i, cf, cp, nota2):
                final_tipo1(i, cf, cp, nota2)
                return True

        #tipo 2

        else:
            # IF
            np = [cf.modo[len(cf.modo) - 1] - 4, cf.modo[len(cf.modo) - 1]]
            random.shuffle(np)
            for i in range(2):
                nota2 = np[i]
                if not filtros(i, cf, cp, nota2):
                    final_tipo2(i, cf, cp, nota2)
                    return True
                    break

    # frigio, mixo, jonico
    else:
        #tipo 1
        if cp.reg == 2:
            nota2 = cf.modo[len(cf.modo) - 1] + 12
            if not filtros(i, cf, cp, nota2):
                final_tipo1(i, cf, cp, nota2)
                return True
        #tipo 2
        else:
            # IF
            np = [cf.modo[len(cf.modo) - 1] - 3, cf.modo[len(cf.modo) - 1]]
            random.shuffle(np)
            for i in range(2):
                nota2 = np[i]
                if not filtros(i, cf, cp, nota2):
                    final_tipo2(i, cf, cp, nota2)
                    return True
                    break

# EXCLUIR VVVVV
# penúltima e última nota
#    if len(cp.notas) == len(cf.modo) - 2:
#        if cp.reg == 2:
#           nota2 = cf.modo[len(cf.modo) - 2] + 9
#            cp.add(nota2)
#            cp.add(cf.modo[len(cf.modo) - 1] + 12)
#            return True
#        #VERIFICAR OITAVA
#        else:
#            nota2 = cf.modo[len(cf.modo) - 2] - 3
#            cp.add(nota2)
#            cp.add(cf.modo[len(cf.modo) - 1])
#            return True
#   else:
#        return False
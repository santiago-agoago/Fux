from dicionario import *

#FILTROS
#regras melódicas
def filt_tess(nota, voz):
    if nota > voz["ma"] or nota < voz["mi"]:
        return True
def filt_rep(i, res, nota):
    if i > 1 and nota == res[i - 1] and nota == res[i - 2]:
        return True
def filt_meldis(i, res, nota):
    if int_mel(res[i - 1], nota) in int_meldis or int_har(res[i - 1], nota) > 12:
        return True
    #regras harmônicas
def filt_saltos(i, res, nota):
    if i >= 3:
        #ascendente
        if int_mel(res[i - 1], nota) > 2 \
                and int_mel(res[i - 2], res[i - 1]) > 2 \
                and int_mel(res[i - 3], res[i - 2]) > 2:
            return True
        #descendente
        if int_mel(res[i - 1], nota) < 2 \
                and int_mel(res[i - 2], res[i - 1]) < 2 \
                and int_mel(res[i - 3], res[i - 2]) < 2:
            return True

#regras harmônicas
def filt_diss(nota1, nota2):
    if abs(nota1 - nota2) not in int_cons:
        return True
    #regras combinadas (Hiller, 1959)

#regras combinadas
def filt_pll(i, cf, res, nota):
    if int_har(cf[i], nota) in conper:
        if int_mel(res[i - 1], nota) >= 1 and int_mel(cf[i - 1], cf[i]) >= 1:
            return True
        if int_mel(res[i - 1], nota) <= 1 and int_mel(cf[i - 1], cf[i]) <= -1:
            return True

    #oitava alcançada por salto (Fux p. 38) (escrever)

#filtros de recomendação (heurísticos)
def filt_grau_conj(i, res, nota, fila):
    if int_har(nota, res[i - 1]) <= 4 and int_har(nota, res[i - 1]) != 0:
        return False
    #permite saltos de acordo com o tamanho da fila e o tamanho do salto. valores devem ser ajustados
    elif len(fila) > 1:
        return False
    else:
        return True


#retorna intervalo
def int_har(nota1, nota2):
    return abs(nota1 - nota2)
def int_mel(nota, notal):
    return notal - nota

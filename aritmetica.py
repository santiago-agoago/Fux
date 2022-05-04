from dicionario import *

#filtros
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

#intervalo
def int_har(nota1, nota2):
    return abs(nota1 - nota2)
def int_mel(nota, notal):
    return notal - nota

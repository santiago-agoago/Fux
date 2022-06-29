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

def filt_ext(res, nota):
    for i in res:
        if int_har(nota, i) > 12:
            return True

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

def filt_cruz(i, cf, res, nota):
    if res.reg == 2 and cf[i] > nota:
        return True

    if res.reg == 1 and cf[i] < nota:
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

# oitavas alcançadas de intervalo superior por salto (Fux p. 38)
def filt_oit(i, cf, res, nota):
    if int_har(cf[i], nota) == 12 and int_har(cf[i - 1], res[i - 1]) >= 14:
        if int_har(cf[i], cf[i - 1]) >= 3 or int_har(nota, res[i - 1]) >= 3:
            return True

# filtros parciais

def filt_grau_conj(i, res, nota, fila):
    # parâmetros ajustáveis
    f = 10
    i_1 = 4
    i_2 = 7

    if int_har(nota, res[i - 1]) <= i_1 and int_har(nota, res[i - 1]) != 0:
        return False
    #permite saltos de acordo com o tamanho da fila e o tamanho do salto. valores devem ser ajustados
    elif len(fila) > f and int_har(nota, res[i - 1]) <= i_2 and int_har(nota, res[i - 1]) != 0:
        return False
    else:
        return True


#retorna intervalo
def int_har(nota1, nota2):
    return abs(nota1 - nota2)
def int_mel(nota, notal):
    return notal - nota
def int_har_mus(nota1,nota2):
    i = int_har(nota1, nota2)

    if i == 0:
        return 0
    if i == 1 or i == 2:
        return 2
    if i == 3 or i == 4:
        return 3
    if i == 5:
        return 4
    if i == 6:
        return "t"
    if i == 7:
        return 5
    if i == 8 or i == 9:
        return 6
    if i == 10 or i == 11:
        return 7
    if i == 12:
        return 8
    if i == 13 or 14:
        return 9
    if i == 15 or 16:
        return 10
    if i == 17:
        return 11
    if i == 18:
        return "t"
    if i == 19:
        return 12

def int_mel_mus(nota2,nota1):
    j = nota2 - nota1

    # sem cruzamento
    if j == 0:
        return "U"
    if j == 1 or j == 2:
        return 2
    if j == 3 or j == 4:
        return 3
    if j == 5:
        return 4
    if j == 6:
        return "t"
    if j == 7:
        return 5
    if j == 8 or j == 9:
        return 6
    if j == 10 or j == 11:
        return 7
    if j == 12:
        return 8
    if j == 13 or j == 14:
        return 9
    if j == 15 or j == 16:
        return 10
    if j == 17:
        return 11
    if j == 18:
        return "t"
    if j == 19:
        return 12

    # com cruzamento
    if j == -1 or j == -2:
        return -2
    if j == -3 or j == -4:
        return -3
    if j == -5:
        return -4
    if j == -6:
        return "t"
    if j == -7:
        return -5
    if j == -8 or j == -9:
        return -6
    if j == -10 or j == -11:
        return -7
    if j == -12:
        return -8
    if j == -13 or j == -14:
        return -9
    if j == -15 or j == -16:
        return -10
    if j == -17:
        return -11
    if j == -18:
        return "t"
    if j == -19:
        return -12
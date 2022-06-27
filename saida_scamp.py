from scamp import *
from dicionario import *
from entrada import *
from main import *

def play(part, lista):
    for n in range(len(lista)):
        part.play_note(lista[n], 0.5, 1)



def run_play(cf, cp):
    global it
    global s
    it = main(cf, cp)
    print(f"|cantus firmus:{cf.modo}\n|resolução:    {cp.notas}")
    print_prim_esp(cf, cp)

    s = Session()
    res_part = s.new_part("organ")
    cf_part = s.new_part("organ")

from main import *
from datetime import *
from dicionario import *

def play(part, lista):
    for n in lista:
        if n in naturais:
            part.play_note(n, 0.5, 4)
        else:
            part.play_note(n, 0.5, 4, "#")

def run_play_trans(cf, cp):
    global it
    global s
    global perf
    it = main(cf, cp)
    print(f"|cantus firmus:{cf.modo}\n"
          f"|resolução:    {cp.notas}")
    print_prim_esp(cf, cp)

    s = Session(tempo=float(200))
    s.fast_forward_in_beats(len(cf.modo) * 4)

    if cp.reg == 2:
        res_part = s.new_part("cp", clef_preference=str(cp.voz["clave"]))
        cf_part = s.new_part("cf", clef_preference=str(cf.voz["clave"]))
    else:
        cf_part = s.new_part("cf", clef_preference=str(cf.voz["clave"]))
        res_part = s.new_part("cp", clef_preference=str(cp.voz["clave"]))

    s.start_transcribing()

    fork(play, args=[cf_part, cf.modo])
    play(res_part, cp.notas)

    s.stop_transcribing().to_score().show()
    return cf.modo, cp.notas

cf, cp = cf_auto()

cf_play, cp_play = run_play(cf, cp)

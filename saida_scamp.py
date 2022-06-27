from scamp import *
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

    dia = date.today().strftime("%m/%d/%y")
    hora = datetime.now().strftime("%H:%M:%S")

    perf = s.stop_transcribing()
    perf.to_score(title=f"{dia}, {hora}", composer="").show()

    wait(10)
    #fork(play, args=[cf_part, cf.modo])
    #play(res_part, cp.notas)

    return cf.modo, cp.notas


cf, cp = cf_auto()

run_play_trans(cf, cp)


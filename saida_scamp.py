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

    s.start_transcribing()

    fork(play, args=[cf_part, cf.modo])
    play(res_part, cp.notas)

    s.stop_transcribing().to_score().show()
    return cf.modo, cp.notas

cf, cp = cf_auto()

cf_play, cp_play = run_play(cf, cp)

while True:
    play = input("Ouvir de novo?\nAperte enter > ")

    if play == "":
        s = Session()

        res_part = s.new_part("organ")
        cf_part = s.new_part("organ")

        fork(play, args=[cf_play, cf_play])
        play(res_part, cp_play)
    else:
        break
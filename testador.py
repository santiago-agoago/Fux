from entrada import *
from main import *
import timeit
from timeit import repeat
from datetime import date
import subprocess

dados = open("dados.txt", "a", encoding = "utf-8")

def get_git() -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()

# resoluções separadas
def run(cf, cp):
    global it
    # print(cf.modo, cf.voz)
    # print(cp.reg, cp.voz)
    it = main(cf, cp)
    print(f"%   |cantus firmus:{cf.modo}\n%    |resolução:    {cp.notas}")
    print_prim_esp(cf, cp,)
    print()


def teste():
    it_total = 0
    start = timeit.default_timer()
    for key, value in cantus_firmi.items():
        if value == lidio:
            cf = CF(value, t)
            print(f"\n–> {key}\n")
            for j in range(2):
                if j == 0:
                    cp = RES(j + 1, b)
                    run(cf, cp)
                    it_total += it
                else:
                    cp = RES(j + 1, a)
                    run(cf, cp)
                    it_total += it
                    print("_________________________________________________")

        else:
            cf = CF(value, a)
            print(f"\n–> {key}\n")
            for j in range(2):
                if j == 0:
                    cp = RES(j + 1, t)
                    run(cf, cp)
                    it_total += it
                else:
                    cp = RES(j + 1, s)
                    run(cf, cp)
                    it_total += it
                    print("_________________________________________________")
    stop = timeit.default_timer()
    tempo_total = round(stop - start, 5)
    print(f"TEMPO TOTAL (s): {tempo_total}")
    print(f"ITERAÇÕES TOTAIS: {it_total}")
    dados.write(f"{date.today()} git: {get_git()} / iterações: {it_total} t = {str(tempo_total)}\n")

#teste()
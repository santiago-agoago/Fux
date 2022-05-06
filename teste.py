from entrada import *
from main import *
import timeit
from datetime import date
dados = open("dados.txt", "a", encoding = "utf-8")

def run(cf, cp):
    # print(cf.modo, cf.voz)
    # print(cp.reg, cp.voz)
    main(cf, cp)
    print(f"|cantus firmus:{cf.modo}\n|resolução:    {cp.notas}")
    print_prim_esp(cf, cp,)
    print()

def teste():
    start = timeit.default_timer()
    for key, value in cantus_firmi.items():
        if value == lidio:
            cf = CF(value, t)
            print(f"\n–> {key}\n")
            for j in range(2):
                if j == 0:
                    cp = RES(j + 1, b)
                    run(cf, cp)
                else:
                    cp = RES(j + 1, a)
                    run(cf, cp)
                    print("_________________________________________________")

        else:
            cf = CF(value, a)
            print(f"\n–> {key}\n")
            for j in range(2):
                if j == 0:
                    cp = RES(j + 1, t)
                    run(cf, cp)
                else:
                    cp = RES(j + 1, s)
                    run(cf, cp)
                    print("_________________________________________________")
    stop = timeit.default_timer()
    tempo_total = round(stop - start, 2)
    print(f"TEMPO TOTAL (s): {tempo_total}")
    dados.write(f"{date.today()}: {str(tempo_total)}\n")

teste()
from entrada import *
from main import *
import timeit
from timeit import repeat
from datetime import *
import subprocess

dados = open("dados.txt", "a", encoding = "utf-8")

def get_git() -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()

def run2(cf, cp):
    global it
    # print(cf.modo, cf.voz)
    # print(cp.reg, cp.voz)
    it = main(cf, cp)
    print(f"%   |cantus firmus:{cf.modo}\n%   |resolução:    {cp.notas}")
    print_prim_esp_seq(cf, cp,)
    print()


def teste():
    start = timeit.default_timer()
    it_total = 0
    lista = [1, 0]
    dia = date.today().strftime("%d/%m/%y")
    hora = datetime.now().strftime("%H:%M:%S")
    print(
        "% % % % % % % % % % % % % % % % % % %\n"
        "\n\\version \"2.22.2\" \n\\language \"portugues\" \n"
        "\n\\header {"
        f"\n    title = \"{dia}, {hora}\""
        f"\n    subtitle = \"Contrapontos de primeira espécie gerados por computador\""
        f"\n    composer = \"Versão git: {get_git()}\""
        "\n}"
    )
    for key, value in cantus_firmi.items():
        if value == lidio:
            cf = CF(value, t)
            print(f"\n%–> {key}\n")
            for j in lista:
                if j == 0:
                    cp = RES(j + 1, b)
                    run2(cf, cp)
                    it_total += it

                else:
                    cp = RES(j + 1, a)
                    run2(cf, cp)
                    it_total += it

        else:
            cf = CF(value, a)
            print(f"\n%–> {key}\n")
            for j in lista:
                if j == 0:
                    cp = RES(j + 1, t)
                    run2(cf, cp)
                    it_total += it

                else:
                    cp = RES(j + 1, s)
                    run2(cf, cp)
                    it_total += it

    print("}\n% % % % % % % % % % % % % % % % % % %")
    stop = timeit.default_timer()
    tempo_total = round(stop - start, 5)
    print(
        f"TEMPO TOTAL (s): {tempo_total}\n"
        f"ITERAÇÕES TOTAIS: {it_total}"
    )
    dados.write(f"{date.today()} git: {get_git()} / iterações: {it_total} t = {str(tempo_total)}\n")

teste()
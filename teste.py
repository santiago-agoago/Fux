from entrada import *
from main import *

def teste():
    for i in range(6):
        if cantus_firmi[i] == lidio:
            cf = CF(cantus_firmi[i], t)
            for j in range(2):
                if j == 0:
                    cp = RES(j + 1, b)
                    #print(cf.modo, cf.voz)
                    #print(cp.reg, cp.voz)
                    main(cf, cp)
                    print(f"cantus firmus:{cf.modo}\nresolução:    {cp.notas}")
                    print_prim_esp(cf, cp,)
                    print("\n")

                else:
                    cp = RES(j + 1, a)
                    #print(cf.modo, cf.voz)
                    #print(cp.reg, cp.voz)
                    main(cf, cp)
                    print(f"cantus firmus:{cf.modo}\nresolução:    {cp.notas}")
                    print_prim_esp(cf, cp,)
                    print("\n")

        else:
            cf = CF(cantus_firmi[i], a)
            for j in range(2):
                if j == 0:
                    cp = RES(j + 1, t)
                    #print(cf.modo, cf.voz)
                    #print(cp.reg, cp.voz)
                    main(cf, cp)
                    print(f"cantus firmus:{cf.modo}\nresolução:    {cp.notas}")
                    print_prim_esp(cf, cp, )
                    print("\n")
                else:
                    cp = RES(j + 1, s)
                    #print(cf.modo, cf.voz)
                    #print(cp.reg, cp.voz)
                    main(cf, cp)
                    print(f"cantus firmus:{cf.modo}\nresolução:    {cp.notas}")
                    print_prim_esp(cf, cp, )
                    print("\n")

teste()


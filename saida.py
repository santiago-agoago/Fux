from entrada import *
from dicionario import *
from aritmetica import int_har_mus, int_mel_mus

#print
def print_prim_esp(cf, cp):
    if cp.reg == 2:
        print("\n\\version \"2.22.2\"\n\\language \"portugues\" \n<<\n\\new Staff {\n\\clef ", cp.voz["clave"])
        for i in range(len(cp.notas)):
            print(midi_ly[cp.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n\\new Staff \with {instrumentName = \"CF\"}\n{\n\\clef", cf.voz["clave"])
        for i in range(len(cf.modo)):
            print(midi_ly[cf.modo[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n>>")
    else:
        print("\n\\version \"2.22.2\"\n\\language \"portugues\" \n<<\n\\new Staff \with { \instrumentName = \"CF\"}\n{\n\\clef", cf.voz["clave"])
        for i in range(len(cf.modo)):
            print(midi_ly[cf.modo[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n\\new Staff {\n\\clef ", cp.voz["clave"])
        for i in range(len(cp.notas)):
            print(midi_ly[cp.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n}\n>>")

def print_prim_esp_seq(cf, cp):
    if cp.reg == 2:
        print("\n    \\new StaffGroup <<\n    \\new Staff {\n    \\clef ", cp.voz["clave"])
        for i in range(len(cp.notas)):
            print("    ", midi_ly[cp.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:

                print("\n    }")

                # intervalos na partitura
                print("    \\addlyrics {", end="")
                for i in range(len(cp.notas)):
                    print("\"", int_mel_mus(cp.notas[i], cf.modo[i]), "\"", sep="", end=" ")
                print("}")

                print("    \\new Staff \with {instrumentName = \"CF\"}\n    {\n    \\clef", cf.voz["clave"])

        for i in range(len(cf.modo)):
            print("    ", midi_ly[cf.modo[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n    }\n    >>")
    else:
        print("\n    \\new StaffGroup <<\n    \\new Staff \with {instrumentName = \"CF\"}\n    {\n    \\clef ", cf.voz["clave"])
        for i in range(len(cf.modo)):
            print("    ", midi_ly[cf.modo[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:

                print("\n    }")

                # intervalos na partitura
                print("    \\addlyrics {", end="")
                for i in range(len(cp.notas)):
                    print("\"", int_mel_mus(cf.modo[i], cp.notas[i]), "\"", sep="", end=" ")
                print("}")

                print("    \\new Staff\n    {\n    \\clef", cp.voz["clave"])

        for i in range(len(cp.notas)):
            print("    ", midi_ly[cp.notas[i]], "1", sep="", end=" ")
            if i == len(cf.modo) - 1:
                print("\n    }\n    >>")
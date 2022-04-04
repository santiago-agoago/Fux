#naipes
s = {"mi" : 60, "ma" : 79}
a = {"mi" : 55, "ma" : 74}
t = {"mi" : 48, "ma" : 67}
b = {"mi" : 40, "ma" : 60}

class Melo:
    def __init__(self, naipe):
        self.naipe = naipe

entrada2 = str(input("> ").lower())
print(entrada2)
if entrada2 == "s":
    print("soprano")
    contra = Melo(s)
if entrada2 == "a":
    print("alto")
    contra = Melo(a)
if entrada2 == "t":
    print("tenor")
    contra = Melo(t)
if entrada2 == "b":
    print("baixo")
    contra = Melo(b)

print(contra.naipe)
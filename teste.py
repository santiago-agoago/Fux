lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


lista2 =[]
completou = False

while completou == False:
    lista2.append("a")
    for i in range(len(lista1)):
        i += 1
        if i == len(lista1):
            lista2.append(lista2[0])
            print(lista2)
            completou = True
            break
        else:
            lista2.append(i)
from matplotlib import pyplot as plt
import numpy as np
import statistics

dados = open("dados.txt", "r")

x_vb = []
y_vb = []
git1 = 0
x = 0
#for line in dados:
#    x += 1
#    x_vb.append(x)
#    for i in range(len(line)):
#        if line[i] == "t":
#            y = i + 4
#    y_vb.append(float(line[y:-1]))

#print(x_vb, y_vb)

x_vm =[]
y_vm = []
y_p = []
x = 0

for line in dados:
    git2 = line[16:23]

    for i in range(len(line)):
        if line[i] == "=":
            y = i + 2

    y_p.append(float(line[y:-1]))

    if git2 != git1:
        x += 0.01
        x_vm.append(x)
        git1 = git2
        y_vm.append(statistics.mean(y_p))
        y_p = []

print(x_vm, y_vm)

plt.plot(x_vm, y_vm)
plt.show()

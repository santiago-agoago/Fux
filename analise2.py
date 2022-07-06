from matplotlib import pyplot as plt
import numpy as np
import statistics

dados = open("dados.txt", "r")

x_b = []
y_b = []
z_b = []
git1 = 0
x = 0

for line in dados:
    x_b.append(line[5:9])
    for i in range(len(line)):
        if line[i] == "t":
            y = i
    y_b.append(float(line[y + 4:-1]))
    z_b.append(float(line[37:y - 1]))


print(x_b)
print(y_b)
print(z_b)

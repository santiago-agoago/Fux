from matplotlib import pyplot as plt
import numpy as np
import statistics

dados = open("dados.txt", "r")

x = []
y = []

for line in dados:
    x.append(line[16:23])
    for i in range(len(line)):
        if line[i] == "t":
            y_i = i + 4
    y.append(line[y_i:y_i + 4])

print(x, y)
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
    x += 1
    x_b.append(x)
    for i in range(len(line)):
        if line[i] == "t":
            y = i
    z_b.append(float(line[y + 4:-1]))
    y_b.append(float(line[37:y - 1]) * 0.00001)

plt.plot(x_b, y_b)
plt.plot(x_b, z_b)
plt.xlabel("Execuções")
plt.ylabel("Tempo de execução (segundos)")
plt.show()

print(x_b)
print(y_b)
print(z_b)

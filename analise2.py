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

fig, ax1 = plt.subplots()


ax1.plot(x_b, y_b, color="blue", label="Iterações do loop principal")
ax1.set_ylabel("x10^4", color="blue")
ax1.set_xlabel("Execuções")
ax1.legend(loc="upper left")
ax2 = ax1.twinx()
ax2.plot(x_b, z_b, color="red", label="Tempo de execução")
ax2.set_ylabel("Segundos", color="red")
ax2.legend(loc="upper right")

plt.show()



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


ax1.plot(x_b, y_b)
ax1.set_ylabel("x10^-5")
ax1.set_xlabel("Execuções")
ax1.legend("Iterações do loop principal por execução", loc="upper left")
ax2 = ax1.twinx()
ax2.plot(x_b, z_b, color="orange")
ax2.set_ylabel("Segundos", color="orange")
ax2.legend("Tempo de execução", loc="upper right")
plt.show()

print(x_b)
print(y_b)
print(z_b)

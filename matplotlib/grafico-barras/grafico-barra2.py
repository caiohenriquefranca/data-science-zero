# Um gráfico de barras também pode ser uma boa opção para plotar histogramas de valores númericos agrupados e representar visualmente a distribuição dos valores

from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Agrupe as notas por decil. mas coloque o 100 com o 99
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar(
    [x + 5 for x in histogram.keys()],  # mova as barras para a direita em 5
    histogram.values(),  # Atribua a altura correta a cada barra
    10,  # Atribua a largura 10 a cada barra
    edgecolor=(0, 0, 0),
)  # Escureça as bordas das barras

plt.axis([-5, 105, 0, 5])  # eixo x de -5 a 105, eixo y de 0 a 5

plt.xticks([10 * i for i in range(11)])  # rótulos de eixo x em 0, 10, ....., 100
plt.xlabel("Decline")
plt.ylabel("# of Students")
plt.title("Distributtion of Exam 1 Grades")
plt.show()

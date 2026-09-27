from matplotlib import pyplot as plt

years = [1950, 1960, 1980, 1990, 2000, 2010, 2015]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# crie um gráfico de linhas, anos no eixo x, gdp no eixo y
plt.plot(years, gdp, color="green", marker="o", linestyle="solid")

# adicione um título
plt.title("Nominal GDP")

# adicione um rótulo ao eixo y
plt.ylabel("Billions of $")
plt.show()

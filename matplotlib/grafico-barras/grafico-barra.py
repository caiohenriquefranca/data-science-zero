# Grafico de barras no Matplotlib serve para comparar valores entre diferentes categorias de forma visual, clara e direta.

from matplotlib import pyplot as plt
# representa o número de Oscars recebido pelos filmes indicados:

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plote as barras com coordenadas x à esquerda [0,1,2,3,4], alturas [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")  # adiciona um título
plt.ylabel("# of Academy Awards")  # rotule o eixo y

# rotule o eixo x com os nom,es dos filmes nos centros das barras
plt.xticks(range(len(movies)), movies)

plt.show()

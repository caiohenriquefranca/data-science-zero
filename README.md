# data-science-zero

A personal educational notebook for data science: small, practical examples built while working through the exercises and ideas of *Data Science from Scratch* by Joel Grus.

Everything here is meant to be run. Each entry is a focused study note — the code, what it demonstrates, what I learned from writing it, and follow-up exercises to consolidate it. The goal is not to cover a library or a tool, but to understand how the underlying ideas work well enough to reimplement them from scratch.

This repository doubles as a study log: it grows as the learning progresses, one topic at a time.

## How this notebook is organized

Notes live in topic folders, and each topic usually exists twice: an interactive `.ipynb` notebook (for reading the code alongside the rendered output) and a plain `.py` script (for keeping the final, minimal version of the exercise).

Every new entry in `README.md` follows the same template, so the log stays easy to scan:

````markdown
### NN — Topic name

- **Source:** chapter or section of the book
- **Goal:** one line describing what this entry practices
- **Code:**

  ```python
  # the minimal example that captures the idea
  ```

- **What I learned:** bullet takeaways
- **Exercises:** small tasks to repeat the idea without copying the solution
````

## Repository layout

```text
data-science-zero/
├── matplotlib/              # Data visualization with Matplotlib
│   ├── grafico-linha/       # Line charts: one value evolving over time
│   └── grafico-barras/      # Bar charts and histogram-like groupings
├── projetos/                # Longer, multi-step exercises
│   └── conector-keys/       # Friends, interests and salaries with collections
└── README.md                # This study log
```

## Contents

1. [Line charts with Matplotlib](matplotlib/grafico-linha/grafico-linha.ipynb) — plotting a series over time, styling, labels
   - [Script version](matplotlib/grafico-linha/grafico-linha.py)
2. [Bar charts with Matplotlib](matplotlib/grafico-barras/grafico-barra.ipynb) — comparing values across categories
   - [Script version](matplotlib/grafico-barras/grafico-barra.py)
3. [Histograms built from bar charts](matplotlib/grafico-barras/grafico-barra2.ipynb) — grouping numeric values with `Counter`
   - [Script version](matplotlib/grafico-barras/grafico-barra2.py)
4. [Connector Keys](projetos/conector-keys/main.py) — friends of friends, shared interests and salaries using `Counter` and `defaultdict`

## Next up

- [ ] Scatter plots and multiple series on the same chart
- [ ] Subplots and figure layout
- [ ] NumPy basics: vectors, matrices and broadcasting
- [ ] pandas basics: loading data, filtering and grouping
- [ ] Descriptive statistics: mean, median, variance and standard deviation
- [ ] Probability distributions and sampling
- [ ] Linear regression implemented from scratch
- [ ] Gradient descent from scratch
- [ ] k-nearest neighbors
- [ ] Decision trees

## Reference

- Joel Grus, *Data Science from Scratch* — O'Reilly, 2nd edition (2019)
- Portuguese edition: *Data Science do Zero* — Alta Books
- Matplotlib documentation: https://matplotlib.org/stable/

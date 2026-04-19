import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Importar el dataset en un DataFrame
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Crear gráfico de dispersión con matplotlib
    # Eje X → Year
    # Eje Y → nivel del mar ajustado
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Primera regresión lineal (todos los datos: 1880 → presente)
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Extender años hasta 2050 para proyección
    years_extended = pd.Series(range(1880, 2051))

    # Calcular valores de la recta (y = mx + b)
    line1 = result.slope * years_extended + result.intercept

    # Dibujar línea de mejor ajuste completa
    plt.plot(years_extended, line1, 'r', label="Best fit (all data)")

    # 4. Segunda regresión (solo desde el año 2000)
    df_recent = df[df["Year"] >= 2000]

    result2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

    # Extender hasta 2050
    years_recent = pd.Series(range(2000, 2051))

    # Calcular segunda línea de tendencia
    line2 = result2.slope * years_recent + result2.intercept

    # Dibujar segunda línea
    plt.plot(years_recent, line2, 'g', label="Best fit (2000 onward)")

    # 5. Configurar etiquetas y título del gráfico
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Mostrar leyenda
    plt.legend()

    # 6. Guardar gráfico
    plt.savefig("sea_level_plot.png")

    # Retornar eje para testing
    return plt.gca()
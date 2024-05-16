import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns 

# Lee el archivo CSV y guárdalo en la variable c19
c19 = pd.read_csv('datos_nomivac_covid19.csv')
c19.info()

num_filas, num_columnas = c19.shape
print("Cantidad de filas:", num_filas)
print("Cantidad de columnas:", num_columnas)

# Histograma de edades (grupo_etario)
plt.figure(figsize=(8, 6))
sns.histplot(data=c19, x='grupo_etario', bins=10, kde=True)
plt.title('Histograma de Edades')
plt.xlabel('Grupo Etario')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.show()


"""
# Gráfico de barras de jurisdicciones de residencia
plt.figure(figsize=(10, 6))
sns.countplot(data=c19, y='jurisdiccion_residencia', order=c19['jurisdiccion_residencia'].value_counts().index)
plt.title('Cantidad de Personas por Jurisdicción de Residencia')
plt.xlabel('Cantidad de Personas')
plt.ylabel('Jurisdicción de Residencia')
plt.show()

"""
import pandas as pd
import numpy as np
from string import Template


print("Ejercicio 2: [")
# Lee el archivo CSV y guárdalo en la variable expvida
expvida = pd.read_csv('life_expectancy_data.csv')

# Probando que esta trabajando con el archivo
print(expvida.head())
print("] ")

print("Ejercicio 3: [")
# Imprimir el tipo de estructura de datos de la variable expvida
print(type(expvida))
print("]  ")

print("Ejercicio 4: [")
# Obtener la cantidad de filas y columnas en expvida usando .shape
filas, columnas = expvida.shape

print("Cantidad de filas:", filas)
print("Cantidad de columnas:", columnas)
print("]  ")

print("Ejercicio 5: [")
# Obtener el nombre de las columnas en expvida
nombres_columnas = expvida.columns

print("Nombres de las columnas:", nombres_columnas)
print("] ")


print("Ejercicio 6: [")
# Inspeccionar las primeras 10 filas de expvida
primeras_filas = expvida.head(10)

print(primeras_filas)
print("] ")

print("Ejercicio 7: [")
# Inspecciono las ultimas 10 filas de expvida
ultimas_filas = expvida.tail(10)

print(ultimas_filas)
print("] ")

print("Ejercicio 8: [")
# Tipo de datos en cada columna de expvida
tipos_de_datos = expvida.dtypes

print(tipos_de_datos)
print("] ")


print("Ejercicio 9: [")
# Obtengo la cantidad de datos faltantes en cada columna
datos_faltantes_por_columna = expvida.isnull().sum()

print(datos_faltantes_por_columna)
print("] ")


print("Ejercicio 10: [")
# Obtengo el maximo valor de datos faltantes y lo guardo en la variable masnan
datos_faltantes_por_columna = expvida.isnull().sum()
masnan = datos_faltantes_por_columna.max()

# Obtengo la cantidad de filas total
cantidad_total_filas = expvida.shape[0]

# Calcular el porcentaje de datos faltantes en relación con el número total de filas
porcentaje_faltantes = (masnan / cantidad_total_filas) * 100

# Imprimo el maximo porcentaje de datos faltantes. Uso f-strings.
# Usando f-strings
print(f"El máximo porcentaje de datos faltantes es: {porcentaje_faltantes:.2f}%")

# Usando str.format()
print("El máximo porcentaje de datos faltantes es: {:.2f}%".format(porcentaje_faltantes))

#Usando template class 

# Formatear la cadena antes de pasarla a Template
cadena_formateada = "El máximo porcentaje de datos faltantes es: {:.2f}%".format(porcentaje_faltantes)

# Crear un objeto Template y luego sustituir los marcadores de posición
template = Template(cadena_formateada)
print(template.substitute())


print("] ")

print("Ejercicio 11: [")
# Renombrar las columnas
expvida.rename(columns={'Life expectancy ': 'life_expectancy', ' BMI ': 'bmi', 'Measles ': 'measles'}, inplace=True)

# Verificar los cambios
print(expvida.head())
print("] ")



print("Ejercicio 12: [")
# Calcular el promedio de expectativa de vida en general
promedio_expectativa_vida = expvida['life_expectancy'].mean()

print("Promedio de expectativa de vida en general:", promedio_expectativa_vida)
print("] ")


print("Ejercicio 13: [")
# Calcular el promedio de expectativa de vida por país
promedio_expectativa_vida_por_pais = expvida.groupby('Country')['life_expectancy'].mean()

print(promedio_expectativa_vida_por_pais)
print("] ")


print("Ejercicio 14: [")
# Expectativa de vida más alta y más baja usando Pandas
max_expectativa_vida = expvida['life_expectancy'].max()
min_expectativa_vida = expvida['life_expectancy'].min()

print("Expectativa de vida más alta usando Pandas:", max_expectativa_vida)
print("Expectativa de vida más baja usando Pandas:", min_expectativa_vida)

# Expectativa de vida más alta y más baja usando NumPy
max_expectativa_vida_np = np.max(expvida['life_expectancy'])
min_expectativa_vida_np = np.min(expvida['life_expectancy'])

print("Expectativa de vida más alta usando NumPy:", max_expectativa_vida_np)
print("Expectativa de vida más baja usando NumPy:", min_expectativa_vida_np)

# Obtener los países con la expectativa de vida más alta
paises_max = expvida[expvida['life_expectancy'] == max_expectativa_vida]['Country']

# Obtener los países con la expectativa de vida más baja
paises_min = expvida[expvida['life_expectancy'] == min_expectativa_vida]['Country']

print("Países con la expectativa de vida más alta:", paises_max.tolist())
print("Países con la expectativa de vida más baja:", paises_min.tolist())
print("] ")



print("Ejercicio 15: [")
# Obtener las categorías únicas en la columna "Status"
categorias_status = expvida['Status'].unique()

# Contar el número de categorías únicas
num_categorias_status = len(categorias_status)

print("Número de categorías en la columna 'Status':", num_categorias_status)
print("] ")


print("Ejercicio 16: [")
# Contar cuántos países se encuentran en cada categoría de "Status"
paises_por_status = expvida['Status'].value_counts()

print("Número de países en cada categoría de 'Status':")
print(paises_por_status)
print("] ")


print("Ejercicio 17: [")
# Filtrar el DataFrame para obtener solo las filas correspondientes al año 2015
casos_sarampion_2015 = expvida[expvida['Year'] == 2015]

# Contar cuántos países presentaron algún caso de sarampión en el año 2015
cantidad_paises_sarampion_2015 = casos_sarampion_2015['measles'].count()

print("Cantidad de países que presentaron algún caso de sarampión en el año 2015:", cantidad_paises_sarampion_2015)
print("] ")

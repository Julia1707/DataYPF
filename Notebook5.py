#Importar numpy
import numpy as np

# Crear un arreglo de ceros de longitud 12
arreglo_de_ceros = np.zeros(12)

print("Ejercicio 1: ",arreglo_de_ceros)

# Crear un arreglo de ceros de longitud 10
arreglo = np.zeros(10)

# Asignar el valor 10 en la posición número 5
arreglo[5] = 10

print("Ejercicio 2: ",arreglo)

# Crear un arreglo con los números del 10 al 49
arreglo2 = np.arange(10, 50)

print("Ejercicio 3: ",arreglo2)

# Crear un arreglo 2D de forma (3, 3) con los números del 0 al 8
arreglo_2d = np.arange(9).reshape(3, 3)

print("Ejercicio 4: ",arreglo_2d)

# Crear un arreglo de números aleatorios de longitud 100
arreglo_aleatorio = np.random.rand(100)

# Calcular la media y varianza del arreglo
media = np.mean(arreglo_aleatorio)
varianza = np.var(arreglo_aleatorio)
print("Ejercicio 5: ")
print("Media:", media)
print("Varianza:", varianza)

# Calcular la media de un arreglo usando np.sum
arreglo_sum = np.array([3, 12, 53, 4, 9])

media = np.sum(arreglo_sum) / len(arreglo_sum)
print("Ejercicio 6: " )
print("Media:", media)


#Calcular la varianza de un arreglo usando np.sum y np.mean

media2 = np.mean(arreglo_sum)
diferencias_cuadrado = (arreglo_sum - media2) ** 2

varianza = np.sum(diferencias_cuadrado) / len(arreglo_sum)
print("Ejercicio 7: ")
print("Varianza:", varianza)


# Crear un arreglo de números aleatorios distribuidos normalmente
arreglo_aleatorio = np.random.randn(10)  
print("Ejercicio 8: ")
print(arreglo_aleatorio)

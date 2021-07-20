import numpy as np

# Declarar y crear Array de una dimensión y nueve elementos.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
print(arr.size)

#Multiplicar array por una constante
arr = arr * 10
print(arr)

#Crear array de dos dimensiones
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n",arr2d)
print(arr2d.size, "elementos")
print(arr2d.ndim, "dimensiones")

#Crear array de 3 dimensiones
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[10, 2, 3], [4, 5, 6]]])
print("\n",arr3d)
print(arr3d.size, "elementos")
print(arr3d.ndim,"dimensiones")

#Crear array de 6 dimensiones, 'ndmin' para indicar número de dimensiones
arr6d = np.array([1, 2], ndmin=6)
print("\n",arr6d)
print(arr6d.size, "elementos")
print(arr6d.ndim,"dimensiones")

#Acceder a los elementos de un arreglo
print("\n")
print(arr[0])
print(arr[0], arr[1])
print(arr[0] + arr[8])
print(arr[-1])#Acceder a la última posición del array
#Números negativos para acceder a posiciones desde el último elemento hacia atrás
'''
Esto
es un
comentario
de varias
lineas
'''

#Acceder a un elemento de un array de dos dimensiones
print('\n')
print(arr2d)
print(arr2d[0,1])

#Hacer slicing de un array: array[star:end]
#Incluye el elemento start pero no el de end
print('\n')
print(arr)
print(arr[3:6])
print(arr[0:]) #Imprime todo el array
print(arr[:5])#Imprime desde el inicio hasta cierto índice
print(arr[0:9:2])#Tercer número indica el salto de posiciones para imprimir
print(arr[::2])#No hay necesidad de indicar el star y end solo el step


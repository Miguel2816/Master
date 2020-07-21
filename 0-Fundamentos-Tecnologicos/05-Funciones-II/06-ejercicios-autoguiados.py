# Fecha: 08/07/2020

# Ejercicio 1: Partiendo de una lista de cadenas obtener una lista con la longitud de cada cadena.

animals = ['chicken', 'cow', 'snail', 'elephant', 'pig', 'zebra']

new_list = list(map(len,animals))
print(new_list)
print('\n'+'-'*30)

# Ejercicio 2: Crear una lista de personas, en la que cada posición será un diccionario con las claves: nombre
# y tfno. Mostrar por pantalla el nombre de las personas utilizando map y lambda

personas = [
 {
 "nombre": "Juan",
 "tfno": "1234567"
 },
 {
 "nombre": "Pepe",
 "tfno": "222222"
 },
 {
 "nombre": "María",
 "tfno": "33333"
 },
]

nombre = lambda x: x['nombre']
nombre_lista = list(map(nombre, personas))
print(nombre_lista)
print('\n'+'-'*30)

# Ejercicio 3: - Función lambda para calcular el mínimo y otra máximo de una lista de números enteros.
# - Implementar una expresión para calcular factorial. f(n) debería devolver el valor de n! (n! = n
# * (n-1) * (n-2) * ... * 1)
# - Implementar una expresión que dada 2 listas devolverá una nueva lista en la que cada
# elemento es el max() para cada par de las listas de entrada. Por ejemplo, dado [1, 3, 6] y [2, 4,
# 5] el resultado es [2, 4, 6]

from functools import reduce

minimo = lambda x: min(x)
maximo = lambda x,y: max(x,y)

# factorial = reduce(lambda x,y: x*y, range(1, n+1), 1)

a = [1, 3, 6]
b = [2, 4, 5]

max_list = list(map(maximo,a,b))
print(max_list)





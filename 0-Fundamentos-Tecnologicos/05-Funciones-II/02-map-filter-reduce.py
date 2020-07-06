# Fecha: 06/07/2020

# Primer Ejercicio: Transformar elementos de una lista a mayusculas

mascotas = ['alfred', 'tabitha', 'william', 'arla']
mascotas_up = list(map(str.upper, mascotas))
# mascotas_up = list(map(lambda mascotas: mascotas.upper(), mascotas))
print(mascotas_up)

# Segundo Ejercicio: tenemos 5 valores en una lista, cada uno con 5 decimiales.
# Queremos que el primero tenga un decimal, el segundo dos y asi
# La funcion round recibe dos elementos, el valor de circle areas y el del rango
# Si solo pasamos un rango de 1 a 3, nos devolvera solo los dos primeros elementos
# Si una de las listas llega a su fin, la funcion map se detiene y devuelve lo que hay ahecho hasta ese momento

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

print(list(map(round, circle_areas, range(1,7))))

# Tercer Ejercicio: crear parejas de datos en una tupla

strings = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5]

data = list(zip(strings,numbers))
data1 = list(map(lambda x,y: (x,y), strings, numbers))
print(data)
print(data1)

# Cuarto Ejercicio: comprobar de una lista quien ha aprobado un examen
notas= [100,20,30,40,50,60,70,80,90,88,21,67,89]

print(list(filter(lambda x: x> 75,notas)))

# Quinto Ejercicio: un detector de palindromos
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)

# Sexto Ejercicio:
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]
result = reduce(lambda x,y:x+y, numbers, 10)
print(result)

# Septimo Ejercicio:

# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round(x**2,2),my_floats))
filter_result = list(filter(lambda name: len(name) >= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1*num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
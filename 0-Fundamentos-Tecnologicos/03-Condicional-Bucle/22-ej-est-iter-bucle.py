# Fecha: 15/06/2020

# EJERCICIOS CON RANGE

# Primer ejercicio: mostrar en pantalla los números del 1 al 20

for i in range(1,21):
    print(i)

print('\n-------------------------------------------------\n')

# Segundo ejercicio: mostrar en pantalla del 3 al 30 de 3 en 3

for i in range(3,31,3):
    print(i)

print('\n-------------------------------------------------\n')

# Tercer ejercicio: crea una lista con los números anteriores

lista_tres = []
for i in range(3,31,3):
    lista_tres.append(i)
print(lista_tres)

print('\n-------------------------------------------------\n')

# Cuarto ejercicio: mostrar por pantalla el cubo de los números del 1 al 10

lista_cube_tres = []
for i in range(1,11):
    print(i)
    lista_cube_tres.append(i)
print(lista_cube_tres)

print('\n-------------------------------------------------\n')

# EJERCICIOS CON ESTRUCTURAS REPETITIVAS

# Primer ejercicio: pide un número al usuario y muestra su tabla de multiplicar

numero = abs(int(input("Introduce un número para calcular su tabla de multiplicar: ")))
print("La tabla de multiplicar del {} es:".format(numero))
for i in range(1,11):
    mult = numero*i
    print("{} * {} = {}".format(numero,i,mult))

print('\n-------------------------------------------------\n')

# Segundo ejercicio: pide nombre y veces que quiere que le salude. Imprime el saludo tantas veces como diga

nombre = input("Introduce su nombre: ")
veces = int(input("Introduce las veces que quieres que le salude: "))

for i in range(1,veces+1):
    print("Hola {}".format(nombre))

print('\n-------------------------------------------------\n')

# Tercer ejercicio: Suma los 100 primeros y muestra el resultado

suma = 0

for i in range(1,101):
    suma += i
print("La suma de los 100 primeros número es:", suma)


# Cuarto ejercicio: Pide números al usuario ahsta que escriba un número negativo. Imprime cuantos positivos excribió

numero = int(input('Por favor, introduce un número: '))
pos_lista = []
while numero >= 0:
    pos_lista.append(numero)
    numero = int(input('Por favor, introduce un número: '))
print("El usuario ha escrito {} números positivos".format(len(pos_lista)))

print('\n-------------------------------------------------\n')

# Quinto ejercicio: User, admin y contraseña 1234&. Hasta que el usuario no escriba la contraseña, preguntar de nuevo hasta 3 intentos

correct_user = 'admin'
correct_password = '1234&'

user = input('Introduce el usuario: ')
password = input('Introduce la contraseña: ')

intentos = [1]

while (correct_user != user or correct_password != password) and len(intentos) <= 3:
    print(len(intentos))
    if correct_user != user and correct_password != password:
        user = input('Usuario y contraseña incorrectos. Introduce el usuario de nuevo: ')
        password = input('Introduce la contraseña: ')
        intentos.append(1)
    elif correct_user != user and correct_password == password:
        user = input('Usuario incorrecto. Introduce el usuario de nuevo: ')
        intentos.append(1)
    elif correct_user == user and correct_password != password:
        password = input('Contraseña incorrecta. Introduce la contraseña de nuevo: ')
        intentos.append(1)

if correct_user == user and correct_password == password:
    print('Usuario y Contraseña correctas!')
else:
    print('Número de intentos agotado')
    
print('\n-------------------------------------------------\n')


# EJERCICIOS CON ESTRUCTURAS SELECTIVAS Y REPETITIVAS

# Primer ejercicio: crea lista magicians y muestra de forma iterativa

magicians = ['alice', 'carolina', 'anne']
for i in magicians:
    print(i)

print('\n-------------------------------------------------\n')

# Segundo ejercicio: crea lista favorite ingredients

favorite_ingredients = ['pepperoni', 'hawaiian', 'veggie']
for i in favorite_ingredients:
    print('I love {} in pizza'.format(i))
print('I love all pizzas')

print('\n-------------------------------------------------\n')

# EJERCICIOS ESTRUCTURAS DE CONTROL Y TIPOS DE DATOS

# Primer ejercicio: crea un tupla con los meses del año, pide números al usuario, y muestra el contenido de esa tupla o error

numero = int(input('Introduce un número: '))

tupla = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

while numero != 0:
    try:
        print(tupla[numero])
        numero = int(input('Introduce un número: '))
    except Exception as e:
        print(e)
        numero = int(input('Introduce un número: '))


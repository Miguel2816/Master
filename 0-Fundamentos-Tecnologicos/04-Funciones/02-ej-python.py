# Fecha 23/06/2020

# Primer Ejercicio: determinar el mayor de tres numeros

lista_num = []

while len(lista_num) < 3:
    num = int(input('Por favor, introduce un numero: '))
    lista_num.append(num)

print('El maximo de la lista {} es {}'.format(lista_num, max(lista_num)))

# Segundo Ejercicio: calcular salario bruto en funcion del numero de horas

horas = float(input('Introduce el numero de horas: '))
precio_hora = float(input('Introduce el precio por hora: '))

if horas > 40:
    print('El salario bruto semanal es: {}'.format(40*precio_hora+(horas-40)*precio_hora*1.5))
else:
    print('El salario bruto semanal es: {}'.format(horas*precio_hora))

# Tercer Ejercicio: solicite numeros hasta introducir -9999 y media de ellos

num_corr = -9999
num = int(input('Introduce un num entero: '))
lista_num = []

while num != num_corr:
    lista_num.append(num)
    num = int(input('Introduce un num entero: '))
print('La media de los numeros de la lista {} es {}'.format(lista_num,(sum(lista_num)/len(lista_num))))

# Cuarto Ejercicio: sumar pares del 1 al 20

suma = 0
for i in range (2,21,2):
    suma +=i
print(suma)

# Quinto Ejercicio: sumar multiplos de 3 y de 5:

lista_multiplos = []
for i in range(1,201):
    if (i%3==0) & (i%5==0):
        lista_multiplos.append(i)
    else:
        pass
print(lista_multiplos)
print(sum(lista_multiplos))


# Sexto Ejercicio: 50 primeros multiplos de 3 y 5

lista_mult = []

for i in range(1,10000000000000000):
    if (i % 3 == 0) & (i % 5 == 0):
        lista_mult.append(i)
        if len(lista_mult) >= 50:
            break
        else:
            pass
    else:
        pass
print(lista_mult)
print(sum(lista_mult))

# Septimo ejercicio: leer 10 numeros, añadirlos a una lista si son multiplos de 2 o de 3

num_lista = []
while len(num_lista) < 10:
    num_tel = int(input("Introduce un num de telf: "))
    num_lista.append(num_tel)

num_mult = []
for i in num_lista:
    if i%2==0:
        num_mult.append(i)
    elif i%3==0:
        num_mult.append(i)
    else:
        pass
num_mult.sort(reverse=True)
for i in num_mult:
    print(i)
num_mult.clear()

# Octavo Ejercicio: Realizar un programa que escriba las tabls de multiplicar del 1 al 10
for numero in range(1,11):
    print("\nLa tabla de multiplicar del {} es: \n".format(numero))
    for i in range(1,11):
        mult = numero*i
        print("{} * {} = {}".format(numero,i,mult))

# Noveno Ejercicio: modificar de notas numericas a escritas

lista = [2, 3, 4.5, 8.9, 9.3, 5.6, 7.8, 10, 8.2]
print(lista)
for i in lista:
    if i < 5:
        lista[lista.index(i)] = 'Suspenso'
    elif i < 7:
        lista[lista.index(i)] = 'Aprobado'
    elif i < 9:
        lista[lista.index(i)] = 'Notable'
    elif i < 10:
        lista[lista.index(i)] = 'Sobresaliente'
    else:
        lista[lista.index(i)] = 'Matricula de honor'
print(lista)


# Decimo Ejercicio: Recibir un tweet y devolver los hastagh

def extrae_hashtags(texto):
    lista = []
    for palabra in texto.split():
        if palabra[0] == '#':
            lista.append(palabra)
    return lista

tweet = "Inscríbete en el #CallOfData2018 para participar en el #datatón"
hashtags = extrae_hashtags(tweet)
print(hashtags)

# Decimoprimer Ejercicio:

infile = open('11-lee-fichero.txt', 'r')

lista = []
for linea in infile:
    lista.append(linea.split())
print(lista)

infile.close()

# Decimosegundo Ejercicio: sumar dos listas de diferente longitud

def suma_listas(a, b):
    suma = []
    menor = min(len(a), len(b))
    for i in range(menor):
        suma.append(a[i] + b[i])
    if len(a) == menor:
        for elem in range(menor, len(b)):
            suma.append(b[elem])
    else:
        for elem in range(menor, len(a)):
            suma.append(a[elem])
    return suma

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]
print(suma_listas(a, b))

# Decimotercer Ejercicio: Guarde elementos en comun entre dos listas

def elementos_comunes(lista1, lista2):
    comunes = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in comunes:
            comunes.append(elemento)
    return comunes

a = [5, 7, 1, 3, 3]
b = [1, 2, 3, 5, 5]
print(elementos_comunes(a, b))

# Decimocuarto Ejercicio: devolver el numero de elementos comunes entre dos listas

def elementos_comunes_iniciales(lista1, lista2):
    comunes = 0
    menor = min(len(lista1), len(lista2))
    while comunes < menor and lista1[comunes] == lista2[comunes]:
        comunes += 1
    return comunes

a = [1, 2, 3, 4]
b = [1, 2, 3]
print(elementos_comunes_iniciales(a, b))

# Decimoquinto Ejercicio: sumar dos matrices

def suma(matriz1,matriz2):

    suma = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        suma.append(fila)
    return suma

a = [ [1, 2, 3], [1, 2, 3] ]
b = [ [4, 5, 6], [4, 5, 6], [4, 5, 6] ]
print(suma(a, b))

# Decimosexto Ejercicio: Realizar programa que lea palabras hasta que se introduzca "fin"

palabra = input('palabra: ')
suma = 0
menor5 = entre5y10 = mayor10 = 0
while palabra != 'fin':
    suma += 1
    if len(palabra) < 5:
        menor5 += 1
    elif len(palabra) > 4 and len(palabra) < 10:
        entre5y10 += 1
    elif len(palabra) > 9:
        mayor10 += 1
    palabra = input('palabra: ')
print('Palabras longitud menor de 5: ', menor5, ' -> ', menor5 * 100/suma, '%')
print('Palabras longitud entre 5 y 10: ', entre5y10, ' -> ', entre5y10 * 100/suma, '%')
print('Palabras longitud mayor de 10: ', mayor10, ' -> ', mayor10 * 100/suma, '%')
print('Número total de palabras introducidas: ', suma)

# DecimoSeptimo Ejercicio: Realizar programaq que comprueve si una lista esta ordenada

def en_orden_ascendente(lista):
    ordenado = True
    i = 1
    ant = lista[0]
    while i < len(lista) and ordenado:
        if lista[i] < ant:
            ordenado = False
        else:
            ant = lista[i]
            i += 1
    return ordenado

a = [1, 3, 5, 10]
b = [3, 5, 1, 10]
print('a: ', en_orden_ascendente(a))
print('b: ', en_orden_ascendente(b))

# DecimoOCtavo Ejercicio: recibi dicc y lista y devuelve dict con valores de la lista que estan en el primer dict

def limpiar_diccionario(diccionario, lista):
    nuevo_diccionario = {}
    for clave in diccionario.keys():
        if clave in lista:
            nuevo_diccionario[clave] = diccionario[clave]
    return nuevo_diccionario

dic = {'clave 1': 'valor 1', 'clave 2': 'valor 2', 'clave 3': 'valor 3'}
lis = ['clave 1', 'clave 3']
print(limpiar_diccionario(dic, lis))

# Decimonoveno: guardar lista en un dict que contiene como claves nombre de usuarios

def agrega_preferencia(diccionario, persona, preferencia):
    if persona not in diccionario:
        diccionario[persona] = []
    if preferencia not in diccionario[persona]:
        diccionario[persona].append(preferencia)
    return diccionario

d = {'a': [], 'b': [1, 2, 3]}
agrega_preferencia(d, 'a', 1)
agrega_preferencia(d, 'b', 4)
agrega_preferencia(d, 'c', 5)
print(d)

# Vigesimo Ejercicio

cadena = input("Cadena:")
diccionario = {"NÚMEROS":0, "LETRAS":0}
for carater in cadena:
    if carater.isdigit():
        diccionario["NÚMEROS"]+=1
    elif carater.isalpha():
        diccionario["LETRAS"]+=1

print(diccionario)
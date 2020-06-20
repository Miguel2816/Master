# Fecha: 20/06/2020

# Primer Ejercicio
import random

nombre = input('Introduce su nombre: ')
print('Bienvenido {}, vamos a ver si puedes adivinar el número que estoy pensando entre el 1 al 50: '.format(nombre))
num_correcto = random.randint(1, 50)
print(num_correcto)
num = int(input('Introduce un número del 1 al 50: '))
intentos = [1]
while (num != num_correcto) & (len(intentos)<5):
    if num < num_correcto:
        num = int(input('El numero correcto es mas alto. Introduce un número del 1 al 50: '))
        intentos.append(num)
    else:
        num = int(input('El numero correcto es mas bajo. Introduce un número del 1 al 50: '))
        intentos.append(num)

if num != num_correcto:
    print('Lo siento {}, has perdido'.format(nombre))
else:
    print('Enhorabuena {}! Has acertado!'.format(nombre))


# Segundo Ejercicio

import re

diccionario = {'Letras': 0,'Numeros': 0}
cadena = 'Hola, me llamo Miguel y tengo 24 años'
letras = []
num_cadena = []
cadena = re.sub(r'[^\w\s]','',cadena)
cadena = cadena.replace(' ','')

# Se puede usar isdigit() en vez de un bucle
numeros = list(range(10))
for i in range(0,len(numeros)):
    numeros[i] = str(numeros[i])
for i in cadena:
    if i in numeros:
        num_cadena.append(i)
    else:
        letras.append(i)

diccionario['Letras'] = len(letras)
diccionario['Numeros'] = len(num_cadena)

print(diccionario)



# Tercer Ejercicio

dic = {'123456-A': ['Python', 'SQL']}

dni = input('Introduce el dni del estudiante: ')
curso = input('Asiste a un curso? (Si/No): ').lower()
lista_cursos = []
if curso == 'si':
    nombre_curso = input('Introduce el nombre del curso: ')
    lista_cursos.append(nombre_curso)
    otro_curso = input('Asiste a otro curso? (Si/No): ').lower()
    while otro_curso == 'si':
        nombre_curso = input('Introduce el nombre del curso: ')
        lista_cursos.append(nombre_curso)
        otro_curso = input('Asiste a otro curso? (Si/No): ').lower()
    dic[dni] = lista_cursos

    alumno = input('Quieres añadir mas alumnos? (Si/No): ').lower()
    while alumno == 'si':
        dni = input('Introduce el dni del estudiante: ')
        curso = input('Asiste a un curso? (Si/No): ').lower()
        lista_cursos = []
        if curso == 'si':
            nombre_curso = input('Introduce el nombre del curso: ')
            lista_cursos.append(nombre_curso)
            otro_curso = input('Asiste a otro curso? (Si/No): ').lower()
            while otro_curso == 'si':
                nombre_curso = input('Introduce el nombre del curso: ')
                lista_cursos.append(nombre_curso)
                otro_curso = input('Asiste a otro curso? (Si/No): ').lower()
            dic[dni] = lista_cursos
            alumno = input('Quieres añadir mas alumnos? (Si/No): ').lower()

        elif curso == 'no':
            alumno = input('Quieres añadir mas alumnos? (Si/No): ').lower()
            dic[dni] = []

elif curso == 'no':
    dic[dni] = []
    alumno = input('Quieres añadir mas alumnos? (Si/No): ').lower()
    while alumno == 'si':
        dni = input('Introduce el dni del estudiante: ')
        curso = input('Asiste a un curso? (Si/No): ').lower()
        lista_cursos = []
        if curso == 'si':
            nombre_curso = input('Introduce el nombre del curso: ')
            lista_cursos.append(nombre_curso)
            otro_curso = input('Asiste a otro curso? (Si/No): ').lower()
            while otro_curso == 'si':
                nombre_curso = input('Introduce el nombre del curso: ')
                lista_cursos.append(nombre_curso)
                otro_curso = input('Asiste a otro curso? (Si/No): ').lower()
            dic[dni] = lista_cursos
            alumno = input('Quieres añadir mas alumnos? (Si/No): ').lower()
        elif curso == 'no':
            alumno = input('Quieres añadir mas alumnos? (Si/No): ').lower()
            dic[dni] = []
print(dic)
for key, value in dic.items():
    print('- DNI: \t {} '.format(key))
    print('\t\t -Numero cursos: {}'.format(len(value)))
    if len(value)>0:
        for i in value:
            print('\t\t -Nombre curso: {}'.format(i))
    else:
        pass


# Cuarto Ejercicio

a = [[1,2,3],[1,2,3],[1,2,3]]
b = [[4,5,6],[4,5,6],[4,5,6]]
c = []

for i, j in zip(a,b):

    zipped_lists = zip(i,j)
    sum = [x + y for (x,y) in zipped_lists]
    c.append(sum)
print(c)

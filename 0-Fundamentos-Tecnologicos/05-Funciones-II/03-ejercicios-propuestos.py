# Fecha: 06/07/2020

# Primer Ejercicio: funcion lambda que calcule el area de un circulo
import math

pi = math.pi
area = lambda r,pi: pi*(r**2)
print(round(area(2,pi),2))

# Segundo Ejercicio: funcion lambda que calcule el cubo de un numero

cubo = lambda x: x**3
print(cubo(3))

# Tercer Ejercicio: funcion lambda que calcule el cuadrado de un numero

cuadrado = lambda x: x**2
print(cuadrado(3))

# Cuarto Ejercicio: funcion lambda que eleve un numero x a otro numero y

potencia = lambda x,y: x**y
print(potencia(3,2))

# Quinto Ejercicio: función lambda que te indique si un número es impar

impar = lambda x: x%2 != 0
print(impar(3))

# Sexto Ejercicio: funcion lambda que invierta una cadena
invertir = lambda cadena:cadena[::-1]
print(invertir("Hola a todos"))

# Septimo-Octavo Ejercicio: función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
# Url: http://aprendeconalf.es/python/ejercicios/programacion-funcional.html
# Escribir una función reciba un diccionario con las asignaturas
# y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.

def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    subjects = map(str.upper, scores.keys())
    grades = map(grade, scores.values())
    return dict(zip(subjects, grades))

print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))




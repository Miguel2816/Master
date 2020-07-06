# Fecha 23/06/2020

# Ejercicios de funciones

# Primer ejercicio: funcion que determine si un numero es impar

def impar(num):
    """
    :param num: numero a determinar si es impar o no
    :return: True/False
    """
    if num%2 ==0:
        print('El numero {} es par.'.format(num))
    else:
        print('El numero {} no es par.'.format(num))

# Segundo Ejercicio: funcion para calcular impuestos en funcion del ingreso e hijos
# Impuesto es un tercio del ingreso imponible
# El ingreso imponible es ingresos totales menos deduccion de 600 y deduccion de 60 por hijo

def impuestos(ingresos, hijos):
    """
    :param ingresos: salario
    :param hijos: numero de hijos
    :return: impuestos
    """
    deduccion_fija = 600
    deduccion_hijo = 60

    return round(((ingresos-deduccion_fija-(deduccion_hijo*hijos))/3),2)

ingresos_totales= 2000
hijos=2
print("El numero de impuestos a pagar por ingresos totales de {} euros y {} hijos es {} euros.".format(ingresos_totales,
                                                                                                       hijos,
                                                                                                       impuestos(ingresos_totales,hijos)))

# Tercer Ejercicio: calcular area y perimetro a partir del radio
# perimetro = 2*pi*r
# area = pi*(r**2)

import math

pi = math.pi

def perimetro(radio):
    """
    :param radio: radio del circulo en cm
    :return: perimetro del circulo en cm
    """
    return round((2*pi*radio),2)

def area(radio):
    """
    :param radio: radio del ciruclo en cm.
    :return: area del circulo den cm2.
    """
    return round((pi*(radio**2)),2)

radio = int(input('Por favor, introduce el radio del circulo en cm: '))

print("Dado un circulo de radio {} cm, su area son {} cm cuadrados y su permietro es de {} cm.".format(radio,
                                                                                                       area(radio),
                                                                                                       perimetro(radio)))

# Cuarto Ejercicio: funcion fuerza calculada a partir de masa y aceleracion
# m/s2

def fuerza(masa, aceleracion):
    """
    :param masa: masa en kg
    :param aceleracion: a en m/s2
    :return:
    """
    return round(masa*aceleracion)

masa = int(input('Introduce la masa en kg: '))
aceleracion = int(input("Introduce la aceleracion en m/s2: "))
print("La fuerza en Newtons de un cuerpo de masa {} kg y aceleracion {} m/s2 es {}.".format(masa, aceleracion,
                                                                                            fuerza(masa,aceleracion)))

# Quinto Ejercicio: calcular el area de distinas figuras, elige figura y se le piden datos

import math

pi = math.pi

def circulo(radio):
    """
    :param radio: radio del circulo en cm
    :return: area del circulo en cm2
    """
    return round((pi*(radio**2)),2)

def cuadrado(lado):
    """
    :param lado: dimension del lado del cuadrado en cm
    :return: area del cuadrado en cm2
    """
    return round((lado*lado),2)

def triangulo(base,altura):
    """
    :param base: base del triangulo en cm
    :param altura: altura del triangulo en cm
    :return: area del triangulo en cm2
    """
    return round(((base*altura)/2),2)

def areas():
    """
    Pide al usuario la figura, y calcula su area.
    :return:
    """
    figura = input("Por favor, introduce el numero (1,2,3) de la figura de la que quieran calcular su area:\n1 Circulo\n2 Cuadrado\n3 Triangulo: ")

    while figura not in ['1','2','3']:
        figura = input(
            "Por favor, introduce el numero (1,2,3) de la figura de la que quieran calcular su area:\n1 Circulo\n2 Cuadrado\n3 Triangulo: ")

    figura = int(figura)
    if figura == 1:
        radio = int(input('Por favor, introduce el radio del circulo en cm: '))
        return ('Ciruclo',circulo(radio))
    elif figura == 2:
        lado = int(input('Introduce la dimension del lado del cuadrado en cm: '))
        return ('Cuadrado',cuadrado(lado))
    elif figura == 3:
        base = int(input('Introduce la base del triangulo en cm: '))
        altura = int(input('Introduce la altura del triangulo en cm: '))
        return ('Triangulo',triangulo(base, altura))

figura, area = areas()
print('El area del {} es de {} cm2.'.format(figura,area))

# Sexto Ejercicio: Leer nota de tres alumnos y mostrar media de las tres.

num_alumnos = int(input("introduce el num de alumnos: "))

def notas(num_alumnos):
    """
    :param num_alumnos: numero de alumnos a pedir nota
    :return: lista de notas de los alumnos
    """
    lista_notas = []
    num_notas = 1
    while num_notas <= num_alumnos:
        nota = round(float(input('Introduce la nota del alumno: ')),2)
        lista_notas.append(nota)
        num_notas += 1
    return lista_notas

def media(lista_notas):
    """
    :param lista_notas: lista d enotas completa
    :return: media de los alumnos
    """
    return round((sum(lista_notas)/len(lista_notas)),2)

print("La media de las notas de los alumnos es {}".format(media(notas(num_alumnos))))

# Septimo Ejercicio: Funcion que convierta radianes en grados

import math
pi = math.pi

def rad_to_grados(radianes):
    """
    :param radianes: radianes a transformar a grados
    :return: transformacion a grados
    """
    return round(((360*radianes)/(2*pi)),2)

radianes = pi
print('{} radianes son {} grados'.format(radianes, rad_to_grados(radianes)))

# Octavo Ejercicio: solicitar la hora y calcule el numero total de segundos desde la medianoche

hora = int(input('Le vamos a pedir la hora actual, en primer lugar, introduce la hora en formato 24h: '))
minuto = int(input('A continuacion, introduzca el minuto: '))
segundo = int(input('A continuacion, introduzca el segundo: '))

def medianoche(hora,minuto,segundo):
    """
    :param hora:
    :param minuto:
    :param segundo:
    :return:
    """
    return (hora*60*60+minuto*60+segundo)
hora_completa = str(hora)+':'+str(minuto)+':'+str(segundo)
print('Desde la medianoche hasta la hora actual, {}, han pasado {} segundos.'.format(hora_completa,
                                                                                     medianoche(hora,minuto,segundo)))

# Noveno ejercicio: leer longitud en km y mostar su eq en hm, dm y m

km = int(input('Introducr distancia en kilometros: '))

def dist(km):
    """
    :param km:
    :return:
    """
    return (km*10,km*100,km*1000)

hm,dm,m = dist(km)
print('La distancia {} en kilometros es igual a {} hectometros, {} decametros y {} metros'.format(km,hm,dm,m))

# Decimo Ejercicio: Determinar si un punto esta sobre una circunferencia o no

x = float(input('Introduce la coordenada x de su punto: '))
y = float(input('Introduce la coordenada y de su punto: '))

def circunferencia(x,y):
    """
    :param x:
    :param y:
    :return:
    """
    if (round(x**2 + y**2)) == 1000:
        print('El punto ({},{}) se encuentra dentro de la cirucunferencia x2+y2=1000.'.format(x,y))
    else:
        print('El punto ({},{}) no se encuentra dentro de la cirucunferencia x2+y2=1000.'.format(x,y))

circunferencia(x,y)

# Undecimo Ejercicio: numero de pintas que contiene una cantidad de fluidos

def pinta_to_ml(pinta):
    """
    :param pinta:
    :return:
    """
    return pinta*473.176473

pinta = float(input('Introduce el numero de pintas: '))
print('{} pintas equivalen a {} ml'.format(pinta,pinta_to_ml(pinta)))

# Duodecimo ejercicio

numero = abs(int(input("Introduce un número para calcular su tabla de multiplicar: ")))
print("La tabla de multiplicar del {} es:".format(numero))
for i in range(1,11):
    mult = numero*i
    print("{} * {} = {}".format(numero,i,mult))

# Trigesimo Ejercicio: calcular distancia entre puntos 3d

import math

a = (4,4,4)
b = (2,2,2)

def dist_3d(a,b):
    """
    :param a: punto de 3 coordenadas
    :param b: punto de tres coordenadas
    :return:
    """
    return (math.sqrt(abs((b[0]-a[0])+(b[1]-a[1])+(b[2]-a[2]))))

print('La distancia entre los puntos {} y {} es {}'.format(a,b,dist_3d(a,b)))

# Cuatrigesimo Ejercicio: Programa un año que decida si es o no bisiesto

año = int(input('Introduce un año: '))

def bisiesto(año):
    """
    :param año:
    :return:
    """
    if año%4==0:
        print('El año {} es bisiesto'.format(año))
    else:
        print('El año {} no es bisiesto'.format(año))

bisiesto(año)

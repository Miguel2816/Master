# Fecha: 06/07/2020

# Ejercicio 0: Programa una función que, recibiendo los 3 coeficientes a, b y c de una ecuación de segundo grado,
# calcule el valor del discriminante:

def discriminante(a, b, c):
    """ float,float,float --> float
    OBJ: calcula el discriminante de la ecuación de segundo grado """
    return b ** 2 - 4 * a * c


# Probador 4,5,1
print(discriminante(4, 5, 1))

# Ejercicio 1: Detectar si un numero es multiplo de 3 o no

def multiplo_tres(x):
    """
    :param x: nmumero a calcular si es multiplo de 3
    :return:
    """
    try:
        if x%3==0:
            print('Es multiplo de tres')
        else:
            print('No es multiplo de tres')
    except:
        print('No has introducido un valor adecuado')
multiplo_tres('d')

# Ejercicio 2: calcular el factorial de un numero del 1 al 3

def validate(num):
    """
    :param num:
    :return:
    """
    try:
        while int(num) not in range(0,31):
            num = input('Por favor, introduce un numero del 1 al 30: ')
        return int(num)
    except:
        return '-1'

def factorial(num):
    """
    :param num: numero entre el rango 0 y 30
    :return:
    """
    num = validate(num)
    if num == 0:
        return 0
    elif num == '-1':
        return "No se ha introducido un numero"
    else:
        prod = 1
        for i in range(1,num+1):
            prod *= i
        return prod

print(factorial(-9))

# Ejercicio 3: “Si la compra es superior a 100EUR se aplica un descuento del 5% si se paga al contado, pero si el pago
# es con tarjeta sólo se aplica el 2%”. Asegúrate de que el importe de la compra es un número válido antes de proceder a los cálculos

dto_tarjeta = 0.02
dto_cash = 0.05
pago = input('Introduce si el pago ha sido con tarjeta/cash (1,2): ')
num = input('Introduce el precio de la compra: ')

def validate(num):
    """
    :param num: numero a validar
    :return:
    """
    try:
        while int(num) <= 0:
            num = input('Por favor, introduce un numero mayor que 0: ')
        return int(num)
    except:
        print('No ha introducido un integer en num.')
        return '-1'

def validate_pago(pago):
    """
    :param pago: modo de pago
    :return:
    """
    try:
        pago = int(pago)
        while int(pago) not in [1,2]:
            pago = int(input('Introduce si el pago ha sido con tarjeta/cash (1,2): '))
        return int(pago)
    except:
        print('No ha introducido un integer en pago.')
        return '-1'

def descuento(pago, num):

    num = validate(num)
    pago = validate_pago(pago)
    if pago == 1:
        return num*dto_tarjeta
    elif pago ==2:
        return num*dto_cash

print('El descuento aplicado es de {} euros'.format(descuento(pago, num)))

# Ejercicio 4: Escribe un subprograma que calcule el producto de dos números enteros leídos desde el teclado sin
# utilizar el operador de multiplicación *. Ej: si recibe 2 y 3 devuelve 6; si recibe 2 y 0 devuelve 0; si recibe
# -3 y 2 dará -6. El programa no asumirá que los números son mayores que cero, debiendo validar las entradas.

def multiplica(numero_menor, numero_mayor):
    suma = 0
    for idx in range(0, abs(numero_menor)):
        suma = suma + abs(numero_mayor)
    if numero_mayor < 0 and numero_menor < 0:
        suma = abs(suma)
    elif numero_mayor < 0 or numero_menor < 0:
        suma = -suma
    return suma


# Programa ppal
try:
    n1 = int(input("Num 1: "))
    n2 = int(input("Num 2: "))

except:
    print("Error. Escribe números enteros")
else:
    if n1 != 0 and n2 != 0:
        if abs(n1) <= abs(n2):
            numero_menor = n1
            numero_mayor = n2
        else:
            numero_menor = n2
            numero_mayor = n1
        print("Producto es ", multiplica(numero_menor, numero_mayor))
    else:
        print("Producto es 0")

# Ejercicio 5: Escribe un programa que lea la hora en notación de 24 horas y la devuelva en notación de 12 horas
# (ejemplo: las 18:30 serán las 6:30 PM). Valida las entradas para asegurarte de que se trata de valores en el rango correcto.

hora = input('Introduce la hora en formato 24 horas: ')

def get_hour_minute(hora):
    """
    :param hora: en formato 24 horas
    :return:
    """
    hora = hora.split(':')
    hora = list(map(int,hora))
    return hora

def transform_hour(hora):
    """
    :param hora: en formato 24 horas
    :return:
    """
    hora_list = get_hour_minute(hora)
    if hora_list[0] >= 12:
        hora = hora_list[0]-12
        hora_completa = str(hora) + ':' + str(hora_list[1]) + ' ' + 'PM'
        return hora_completa
    else:
        hora_completa = str(hora_list[0]) + ':' + str(hora_list[1]) + ' ' + 'AM'
        return hora_completa

print(transform_hour(hora))

# Ejercicio 6: Programa una función “validar_entero” que se asegure de que una entrada del usuario es un entero.
# Nuestra función recibirá un texto y retornará verdadero si es un entero (dando por válida la entrada) o falso (rechazando la entrada).

def validar_entero (entrada):
    """
    :param entrada: el valor a calcular si es entero o no
    :return:
    """
    if type(entrada) == int:
        return "Es un numero entero"
    else:
        return "No es un número entero"


print("El numero 5 ", validar_entero(5))
print("El booleano True ", validar_entero(True))
print("El float 5.4 ", validar_entero(5.4))
print("El cadena de caracteres Hola", validar_entero("Hola"))

# Ejercicio 7: Programa una función “validar_real” similar a la del ejercicio anterior pero que valide que una entrada es un número real

def validar_real(entrada):
    """
    :param entrada:
    :return:
    """
    if type(entrada) != float:
        return "No es un numero real"
    else:
        return "Es un numero real"

#Pruebas
print("El numero 5 ", validar_real(5))
print("El booleano True ", validar_real(True))
print("El float 5.4 ", validar_real(5.4))
print("El cadena de caracteres Hola", validar_real("Hola"))

# Ejercicio 8: Programa una función que reciba una calificación numérica y retorne la letra con la nueva calificación.
# A 8.5 o mayor, B 6.5 o mayor, C 5 o mayor, D 3.5 o mayor, F el resto. Funcion de validacion.

def calificaciones(nota):
    """float-->str
    OBJ:Dada una nota saber que calificacion se ha obtenido
    PRE:0<=float<=10"""
    if nota>=8.5:
        return "A"
    elif 6.5<=nota<8.5:
        return "B"
    elif 5<=nota<6.5:
        return "C"
    elif 3.5<=nota<5:
        return "D"
    else:
        return "F"

try:
    nota=float(input("Introduce una nota: "))
except:
    print("Introduzca una nota correcta")
else:
    if 0<=nota<=10:
        print("Con un ",nota," obtienes una", calificaciones(nota))
    else:
        print("Introduce una nota correcta")

# Ejercicio 9: Codifica un subprograma que reciba un número entero, y si es entre 1 y 12 escriba un mensaje por pantalla
# indicando el mes a que dicho número corresponde. En caso contrario deberá mostrar un mensaje de error.

def mes():
    try:
        mes = int(input('Introduce el mes en el que naciste en numero: '))
        if int(mes) in range(1,13):
            meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                    "Noviembre", "Diciembre"]
            mes = meses[mes - 1]
            return mes
        else:
            print('El numero que ha introducido no se corresponde con ningun mes')
    except:
        print('No ha introducido un numero')

print(mes())
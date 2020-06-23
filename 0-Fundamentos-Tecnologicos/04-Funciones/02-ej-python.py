# Fecha 23/06/2020
"""
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
"""
# Noveno Ejercicio: modificar de notas numericas a escritas


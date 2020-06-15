# Fecha: 15/06/2020

# Ejercicios de la parte de estructuras de control selectivas

# Primer ejercicio: pedir la edad e indicar si es mayor de edad o no

mayor_edad = 18
edad = int(input('Introduce su edad: '))
if edad < mayor_edad:
    print('Usted es menor de edad')
else:
    print('Usted es mayor de edad')

print('\n-------------------------------------------------\n')

# Segundo ejercicio: crea la lista favorite_movies. Pedir al usuario una pelicula favoirta y comprobar si coincide con alguna de la lista o no
# Tercer ejercicio: ten en cuenta las minúsculas o mayúsculas

import re
favorite_movies = ['Iron Man', 'Captain America', 'Avengers']
peli = input('Introduce su película favorita: ')
for i in range(0,len(favorite_movies)):
    favorite_movies[i] = favorite_movies[i].lower()

peli = re.sub(' +',' ',peli)
if peli.lower() in favorite_movies:
    print('A los dos nos gusta la misma película: {}'.format(peli))
else:
    print('No nos gustan las mismas películas')

print('\n-------------------------------------------------\n')

# Cuarto ejercicio: La entrada a un museo depende de la edad del visitante.
# Menor de 4, gratis, Hasta 12, 4.5 euros, y a partir de 12 son 8 euros

edad_entrada = int(input('Introduce su edad: '))

if edad_entrada < 4:
    print('Su entrada es gratuita')
elif 4 <= edad_entrada < 12:
    print('Su entrada son 4.5 euros')
elif edad_entrada >= 12:
    print('Su entrada son 8 euros')

print('\n-------------------------------------------------\n')

# Quinto ejercicio: Solicitar la edad y mostrar un mensaje en función de dicha edad

edad_mensaje = int(input('Introduce su edad: '))

if edad_mensaje < 2:
    print('Eres un bebé!')
elif 2 <= edad_mensaje < 4:
    print('Eres un crío!')
elif 4 <= edad_mensaje < 13:
    print('Eres un niño!')
elif 13 <= edad_mensaje < 20:
    print('Eres un adolescente!')
elif 20 <= edad_mensaje < 65:
    print('Eres un adulto!')
else:
    print('Eres un anciano!')

print('\n-------------------------------------------------\n')

# Sexto: escribe un output determinado utilizando un bucle for e if elif else

for i in range(1,10):

    if i == 1:
        print(str(i)+'st')
    elif i == 2:
        print(str(i)+'nd')
    elif i == 3:
        print(str(i)+'rd')
    else:
        print(str(i)+'th')
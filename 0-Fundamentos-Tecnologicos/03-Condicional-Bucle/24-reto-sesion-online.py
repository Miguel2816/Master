# Fecha: 20/06/2020
import random

historia = 'Videojuego primera mision'
print(historia)
jugar = 'si'
while jugar == 'si':

    lista_cabanas = []
    opciones = ('Enemigo', 'Amigo', 'Desocupado')

    for i in range(0,5):
        lista_cabanas.append(random.choice(opciones))

    # tupla = tuple([(1,lista_cabanas[0]), (2,lista_cabanas[1]), (3,lista_cabanas[2]), (4,lista_cabanas[3]), (5,lista_cabanas[4])])
    # tupla = ([(1,lista_cabanas[0]), (2,lista_cabanas[1]), (3,lista_cabanas[2]), (4,lista_cabanas[3]), (5,lista_cabanas[4])])
    #diccionario = {'Cabana1': lista_cabanas[0],
    #               'Cabana2': lista_cabanas[1],
    #               'Cabana3': lista_cabanas[2],
    #               'Cabana4': lista_cabanas[3],
    #               'Cabana5': lista_cabanas[4]}

    lista = [(1,lista_cabanas[0]), (2,lista_cabanas[1]), (3,lista_cabanas[2]), (4,lista_cabanas[3]), (5,lista_cabanas[4])]

    num_cabana = int(input('Introduce el numero de cabana del 1 al 5: '))

    cabana_escogida = lista[num_cabana-1]
    opcion=cabana_escogida[1]

    if opcion == 'Enemigo':
        print('Has perdido. Un salvaje acaba de matarte.')
    elif opcion == 'Amigo':
        print('Has ganado. Puedes descansar.')
    else:
        print('Has ganado. Puedes descansar')
    jugar = input('Quieres jugar otra vez? (Si/No): ').lower()
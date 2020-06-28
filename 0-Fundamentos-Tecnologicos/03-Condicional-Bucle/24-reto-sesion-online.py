# Fecha: 20/06/2020
import random
import textwrap

if __name__ == '__main__':

    ancho = 70
    line = '-'*70

    print(line)
    print('Game of Thrones v0.0.1')
    print(line)

    historia = "Perteneces a la Guardia de la Noche." \
                   "Llevas semanas andando al otro lado del muro," \
                   "en una expedición para detectar posibles salvajes." \
                   "Llegas a un poblado con 5 cabañas." \
                   "Debes elegir en qué cabaña entrarás." \
                   "Si está vacía podrás descansar... pero" \
                   "corres el riesgo de encontrarte con un salvaje y morir…"

    print(textwrap.fill(historia, width=70))

    jugar = 'si'
    while jugar == 'si':

        lista_cabanas = []
        opciones = ('Enemigo', 'Amigo', 'Desocupado')

        for i in range(0,5):
            lista_cabanas.append(random.choice(opciones))

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
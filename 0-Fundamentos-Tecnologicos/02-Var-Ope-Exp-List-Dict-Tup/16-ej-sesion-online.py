# Fecha: 13/06/2020

# Ejercicios de la sesión online. Enunciados en el pdf.

# Primer Ejercicio

a = [4,-70,-30,12,3]

# Mostrar por pantalla el segundo valor de la lista a
print("El segundo elemento de la lista es:",a[1])

# Crea una lista (llamaremos repetidos_a) que almacene tres veces los valores de a
a_rep = a*3
print("La lista inicial repetida 3 veces es:",a_rep)

# Muestra el número de veces que se repite el valor - 70 en la lista repetidos_a
print("El número -70 aparece {} veces.".format(a_rep.count(-70)))

# Muestra de forma ascendente la lista repetidos_a
a_rep.sort()
print("La lista inicial repetida 3 veces ordenada de forma ascendente es:",a_rep)

# Muestra de forma descendente la lista repetidos_a
a_rep.sort(reverse=True)
print("La lista inicial repetida 3 veces ordenada de forma descendente es:",a_rep)

# Elimina los repetidos de la lista (no se pueden usar bucles au nque los conozcas)
print("La lista inicial repetida 3 veces eliminando los repetidos es:",list(set(a_rep)))

# Crear una nueva lista llamada a_sort donde se almacene la lista a ordenada Ten en cuenta que deberás seguir teniendo la listaa original
a_sort = sorted(a)
print("La lista inical ordenada es {} y desordenada es {}.".format(a_sort,a))

# Segundo Ejercicio

# Crea una lista para guardar la información de pedidos # Cada posición de la lista se corresponderá a un mes
# Posición 0 para enero, 1 para febrero...
# La información de cada pedido a su vez es una lista
# con el producto y no unidades
# Escribe los siguientes pedidos dentro de la lista pedidos # Enero ["galletas", 100]
# Febrero ["bicis", 30]

pedidos = [['Enero',['galletas', 100]],['Febrero',['bicis',30]],['Marzo',[]],['Abril',[]],
           ['Mayo',[]],['Junio',[]],['Julio',[]],['Agosto',[]],['Septiembre',[]],['Octubre',[]],
           ['Noviembre',[]],['Diciembre',[]]]

# Muestra los pedidos de Febrero
print("Los pedidos en Febrero son:",pedidos[1])

# Muestra el stock del producto de Enero
print("El stock del producto en Enero es:", pedidos[0][1])

# Pide el nombre de producto y unidades del mes de abril
producto_abril =  input("Introduce el nombre del producto de abril: ")
stock_abril = int(input("Introduce el stock del producto de abril: "))
pedidos_abril = [producto_abril,stock_abril]
pedidos[3][1] = pedidos_abril
print("La lista una vez se ha incluido Abril es:",pedidos)

# Actualiza el stock del producto vendido en Febrero a la mitad
pedidos[1][1][1] = int(pedidos[1][1][1]/2)
print("La lista con el stock de Febrero actualizado es:",pedidos)

# ‘Elimina’ el pedido del mes de enero (deja la lista vacía)
pedidos[0][1] = []
print("La lista sin los pedidos de Enero es:", pedidos)

# Tercer Ejercicio

# Crea un diccionario que simule la agenda
# de un teléfono móvil, donde guardaras:
# - el nombre y apellidos como clave del registro
# - teléfono móvil
# Para ello, crea la variable e introduce los siguientes valores:
# Juan Pérez:1234567
# José Martín: 111111111
# Susana Ruiz:222222

agenda = {
    "Juan Pérez": '1234567',
    "José Martín": '111111111',
    "Susana Ruiz": '2222222'
}

print("Mi agenda es:", agenda)

# Muestra por pantalla el teléfono de Juan
print('El número de Juan es:', agenda["Juan Pérez"])

# Vamos a añadir el teléfono de una nueva persona Paloma del Val
# Pide por consola su número tfno
tel_paloma = (input(("Introduce el teléfono de Paloma del Val: ")))
agenda['Paloma del Val'] = tel_paloma
print('Mi agenda actualizada es:', agenda)

# Vamos añadir un nuevo contacto. Tendrás que pedir por consola # el nombre de la persona y el teléfono
nombre = input(('Vamos a añadir el número de una persona nueva. Por favor, introduce el nombre: '))
tel_nombre = (input(("Introduce el teléfono: ")))
agenda[nombre] = tel_nombre
print('Mi agenda actualizada es:', agenda)

# Modifica el tfno de Paloma del Val por 9999999
agenda['Paloma del Val'] = '9999999'
print('Mi agenda con el número de Paloma actualizado es:', agenda)

# Elimina el tfno de Paloma del Val
del agenda['Paloma del Val']
print('Mi agenda con el número de Paloma eliminado es:', agenda)

# Pide por consola el nombre de un contacto y elimina su tfno
nombre_eliminar = ""

while nombre_eliminar not in list(agenda.keys()):
    nombre_eliminar = input("Introduce uno de los siguientes nombres, para eliminar su contacto: {} ".format(', '.join(list(agenda.keys()))))

del agenda[nombre_eliminar]
print('Mi agenda actualizada es:', agenda)

# Vacía la agenda
agenda.clear()
print(agenda)

# Cuarto Ejercicio

# Vamos a crear una estructura de datos para almacenar aulas
# Cada aula vendrá identificada por su nombre (será unico)
# De cada aula se guardan datos como:capacidad y si tiene proyec tor o no
# Comienza creando las siguientes aulas
# "Leonardo", 23, No tiene proyector
# "Picasso", 35, Si tiene proyector
# "Cajal", 15, Si tiene proyector

aulas = {
    'Leonardo': [23,'No'],
    'Picasso': [35,'Si'],
    "Cajal": [15,'Si']
}

print("Las aulas son:", ', '.join(list(aulas.keys())))

# Muestra la capacidad de alumnos del Aula Leonardo
print('La capacidad del aula Leonardo es:', aulas['Leonardo'][0])

# Muestra si el Aula Picasso tiene proyector
print('¿Tiene proyector el aula Picasso?', aulas['Picasso'][1])

# Añade los datos de una nueva aula, pidiendo los tres datos por consola
aula_nombre = input("Introduce el nombre de un nuevo aula: ")
aula_cap = int(input("Introduce la capacidad del aula: "))
aula_proyector = input("Introduce si el aula tiene proyector (Si/No): ")

aulas[aula_nombre]=[aula_cap,aula_proyector]
print("Las aulas actualizadas son:", aulas)

# Pide el nombre de un aula que exista
# A continuación, cambia el valor de su capacidad al doble
nombre = ""

while nombre not in list(aulas.keys()):
    nombre = input('Introduce uno de los siguientes nombres: {} '.format(', '.join(list(aulas.keys()))))

aulas[nombre][0] = aulas[nombre][0]*2
print(aulas)

# Pide al usuario el nombre de un aula y elimínala
segundo_nombre = ""

while segundo_nombre not in list(aulas.keys()):
    segundo_nombre = input('Introduce uno de los siguientes nombres: {} '.format(', '.join(list(aulas.keys()))))

del aulas[segundo_nombre]
print("Las aulas actualizadas son:", aulas)

# Quinto Ejercicio

# Define una estructura de datos para almacenar clientes.
# La información que se almacenará de cada cliente será:
# cif (será identificador único de cada cliente), nombre,
# dirección, comunidad, pais, tfno, persona contacto, si es pref erente o no
#Pista diccionario de diccionarios
# De momento tendremos 2 clientes con datos de ejemplo:
# "1111-A", "Empresa A", "c\Alcala,23", "Madrid", "España", "1234567", " Juan", False
# "2222-b", "Empresa B", "Avda. Diagonal", "Barcelona", "España", "76543 21", "Susana", True

clientes = {
     '1111-A': {
         "nombre": "Empresa A",
         "direccion": "c\Alcala,23",
         "comunidad": "Madrid",
         "pais": "España",
         "tfno": "1234567",
         "contacto": "Juan",
         "preferente": False
     },
    '2222-B':{
         "nombre": "Empresa B",
         "direccion": "Avda. Diagonal",
         "comunidad": "Barcelona",
         "pais": "España",
         "tfno": "7654321",
         "contacto": "Susana",
         "preferente": True
    }
}

print("La informacion de los clientes es:", clientes)

# Pide por pantalla todos los datos para dar de alta un nuevo cliente
cif = input("Introduce su cif para darse de alta: ")
nombre = input("Introduce su nombre para darse de alta: ")
direccion = input("Introduce su direccion para darse de alta: ")
comunidad = input("Introduce su comunidad para darse de alta: ")
pais = input("Introduce su pais para darse de alta: ")
tfno = input("Introduce su tfno para darse de alta: ")
contacto = input("Introduce su contacto para darse de alta: ")
preferente = bool(input("Introduce su preferente para darse de alta (True/False): "))

nuevo_cliente = {
         "nombre": nombre,
         "direccion": direccion,
         "comunidad": comunidad,
         "pais": pais,
         "tfno": tfno,
         "contacto": contacto,
         "preferente": preferente
    }

clientes[cif]=nuevo_cliente

print("La informacion actualizada de los clientes es:", clientes)

# Pide por pantalla el cif de un cliente y muestra sus datos
cif_pantalla = ''
while cif_pantalla not in list(clientes.keys()):
    cif_pantalla = input("Introduce el cif de la empresa que quieras consultar, debe ser uno de los siguientes: {} ".format(", ".join(list(clientes.keys()))) )
print("La informacion de la empresa con cif {} es: {}".format(cif_pantalla, clientes[cif_pantalla]))

# Pide por pantalla el cif de un cliente, el campo que se desea cambiar y su nuevo valor
cif_modificar = ''
categoria_modificar = ''
while cif_modificar not in list(clientes.keys()):
    cif_modificar = input("Introduce el cif de la empresa cuya info quieras modificar, debe ser uno de los siguientes: {} ".format(", ".join(list(clientes.keys()))) )
while categoria_modificar not in list(nuevo_cliente.keys()):
    categoria_modificar = input("Introduce la categoria de la empresa cuya info quieras modificar, debe ser uno de los siguientes: {} ".format(", ".join(list(nuevo_cliente.keys()))) )
categoria_valor = input("Introduce el nuevo valor de la categoria {}: ".format(categoria_modificar))
clientes[cif_modificar][categoria_modificar] = categoria_valor
print("La info del cliente actualizado es:", clientes[cif_modificar])

# Pide por pantalla el cif de un cliente para eliminarlo
cif_eliminar = ''
while cif_eliminar not in list(clientes.keys()):
    cif_eliminar = input("Introduce el cif de la empresa cuya info quieras eliminar, debe ser uno de los siguientes: {} ".format(", ".join(list(clientes.keys()))) )
del clientes[cif_eliminar]
print("La informacion actualizada de los clientes es:", clientes)

# Pide por pantalla el cif de un cliente y un campo para eliminarlo
cif_cat_eliminar = ''
categoria_eliminar = ''
while cif_cat_eliminar not in list(clientes.keys()):
    cif_cat_eliminar = input("Introduce el cif de la empresa cuya info quieras modificar, debe ser uno de los siguientes: {} ".format(", ".join(list(clientes.keys()))))
while categoria_eliminar not in list(nuevo_cliente.keys()):
    categoria_eliminar = input("Introduce la categoria de la empresa cuya info quieras eliminar, debe ser uno de los siguientes: {} ".format(", ".join(list(nuevo_cliente.keys()))) )
del clientes[cif_cat_eliminar][categoria_eliminar]
print("La informacion actualizada de los clientes es:", clientes)

#Clase: Estructuras repetitivas. Bucle for

# Ejemplo imprimir tres veces el mensaje Hola
print("Ejemplo 1")
for i in [0, 1, 2]:
    print(i,"-Hola")


print()

# Ejemplo 2. En este ejemplo itera sobre una lista de valores que no son numéricos
print("Ejemplo 2")
for amiga in ["Marta", "Luna", "Ana", "Kira", "Patti"]:
    invitacion = amiga + ", te espero en mi fiesta."
    print ( invitacion )

# Uso de función range en los bucles for
# Ejemplo 3. Uso de range en un bucle for
for i in range(10):
    print(i) #en este caso como la función print no se especifica parámetro de final termina con un salto de línea

print()

for i in range (1 ,20):
    print (i, end =" ") #en este otro ejemplo se añade a la función print el parámetro end y finaliza con un espacio en blanco

print()

animals = ["cat", "dog", "lion"] #creamos una lista de animales
for elemento in animals: #con el bucle for se recorre cada elemento que existe en la lista de animales
    print(elemento, end ="/") #añade al final una barra

print()

x = 0
for i in range (1, 10, 2):
    x += i
    print(x)
print (x)

print()

#Ejemplo de un for que itera una cadena
for caracter in "Hola a todos":
    print(caracter)

print("Ejercicio 1: Pedir un número al usuario y mostrar la tabla de multiplicar de dicho número ")
num = int (input("Escribe un número: "))
print("La tabla de multiplicar del número " + str(num) +  "es: ")
for x in range (0,11):
    print(str(num) + " * " + str(x) + " = "+ str(num*x) )



print()
print("Ejercicio 2: mostrar las tablas de multiplicar de los números pares del 1 al 10")
for i in range (2 ,11 ,2):
    for j in range (0 ,11):
        print (i,"x",j,"=",i*j)
    print (" --------------")
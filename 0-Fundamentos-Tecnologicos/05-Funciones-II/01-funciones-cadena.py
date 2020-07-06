#Ejemplo de funciones predefinidas para el trabajo con cadenas en Python

#len longitud de una cadena
saludo="Hola"
print(len(saludo))

#mostrar texto usando caracteres de escape y especificadores
cadena = "Hola esto es una cadena"
print("La variable cadena tiene el mensaje:\n\t %s \n\t %i caracteres" %(cadena, len(cadena)))

#convertir a mayúsculas con upper() y minúsculas con lower()
car="Audi"
print(car.upper()) #convierte a mayúsculas
print(car.lower()) #convierte a minúsculas

#eliminar espacios con strip, lstrip, rstrip
mensaje = "  Yuju  yupi  "
print(mensaje.lstrip()) #elimina espacios en blanco por la izquierda
print(mensaje.rstrip()) #elimina espacios en blanco por la derecha
print(mensaje.strip()) #elimina espacios en blanco p la izquierda y derecha

#reemplazar una palabra por otra con replace
mensaje ="Juan es amigo mío"
mensaje = mensaje.replace("es", "era")
print(mensaje)

#join se utiliza para convertir una lista en cadena
lista = ["Hola", "amigo", "mio"]
cadena = " ".join(lista) #sintaxis es 'separador'.join(nombrelista)
print(cadena, type(cadena))

#función split se utiliza para crear una cadena a partir de una lista
nombre = "Juan Perico Palotes"
lista_nombre = nombre.split() #obtenemos una lista con las palabras de la cadena
print(lista_nombre, type(lista_nombre))


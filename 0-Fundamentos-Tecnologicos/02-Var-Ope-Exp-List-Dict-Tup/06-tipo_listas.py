 # Tipo listas
#  Colección de objetos ordenada y mutable
#  Elementos dentro de [] separados por comas
#  Puede contener distintos tipos de elementos 


print("\nCreación de una lista vacía")
precios =[]
print("\n\nLa lista precios contiene: ")
print(precios)

print("\n\nCreación de una lista de temperaturas (floats)")
temperaturas = [32.0, 23.0, 18.5]
print(temperaturas, type(temperaturas))

print("\n\nCreación de una lista con nombres (strings)")
nombres = ["Juan", "Marcos", "María"]
print(nombres, type(nombres))

print("\n\nCreación de una lista con distintos datos (string, float, int)")
detalle_coche =['Hyundai', 'ix20', 2.2, 23500]
print(detalle_coche, type(detalle_coche))


print("\n\nAcceso a los elementos de la lista")
print("El elemento 0 de la lista nombres es: ", nombres[0])
print("El elemento 1 de la lista nombres es: ", nombres[1])
print("El elemento 0 de la lista detalle_coches es: ", detalle_coche[0])
print("El elemetno 1 de la lista detalle_coches es: ", detalle_coche[1])

print("\n\nListas en su interior pueden contener listas")
coche = ['Hyundai', 'ix20', 23500, ["Diesel","Gasolina", "Híbrido", "Eléctrico"]]

print("\n\nPara acceder a elementos anidados:")
print(" El elemento 2 de la lista tiene otra lista donde el elemento 2 es ", coche[3][2])


# Obtener un rango de elemento especifico
numeros=[1,2,3,4,5,6,7]
print("\n\nLa lista numeros tiene:" ,numeros)
sublista = numeros[0:3]
print ("La sublista 0:3 tiene:", sublista)

# Obtener un rango con saltos de elementos específicos
sublista2 = numeros[0:7:2]
print ("La sublista  0:7:2 tiene: ", sublista2)
sublista3 = numeros[1::2]
print ("La sublista 1::2 tiene:", sublista3)


print("\n\nPodemos convertir una variable cadena a tipo lista: ")
frase="¡No te asustes!"
frase_list=list(frase)

print("La variable frase: ", frase, type(frase))
print("La variable frase_list: ", frase_list, type(frase_list))

print("--OPERACIONES LISTAS")
print("\n\nEjemplo de otra lista de distinto tipo sobre la cual vamos a ver algunas operaciones")
factura = ['huevos','pan',10,50]
print(factura, type(factura))

print("\n\nLos elementos de la lista son:") 
print(factura[0])  #La primera posición es la 0
print(factura[1])
print(factura[2])
print(factura[3])

print("\n\nLos elementos de la lista accediendo por el final son:")
print(factura[-1]) #-1 hace referencia al último elemento
print(factura[-2])
print(factura[-3])
print(factura[-4])

#Cambiar el valor de una posición concreta
print("\n\nModificamos el elemento pan por aceite: ")
factura[1]='aceite'
print(factura)


#Conocer el nº de elementos de la lista
print("\nLa lista tiene %i elementos" %len(factura))



print("\n\nAgregar otro elemento al final de la lista")
factura.append("Carne")
print("\n\nHemos agregado el elemento carne, ahora la lista es:")
print(factura)

print("Contar el nº de veces que aparece un elemento en la lista ")
print("Pan aparece %i veces" %factura.count('pan'))

print("insertamos un nuevo valor en la posición 3")
factura.insert(3,'xx')
print(factura)

print("Ahora lo eliminamos con remove")
factura.remove('xx')
print(factura)


#reverse imprime al revés
print("Método reverse")
factura.reverse()
print(factura)

#pop este método elimina
print("Método pop sin parámetro")
eliminado1=factura.pop() #En este caso no se le especifica, eliminará el último
print("La lista queda: ", factura)
print("El eliminado ha sido ", eliminado1, type(eliminado1))


print("Método pop con parámetro")
eliminado2=factura.pop(2) #En este caso no se le especifica
print("La factura queda: ", factura)
print("El eliminado ha sido ", eliminado2, type(eliminado2))

#método extend coge todos los elementos de otra lista y los incluye en la primera
#se usa para combinar dos listas. Los añade al final
print("Método extend: ")
factura.extend([10,'huevos'])
print("Ahora la lista queda: ", factura)

print("¿Qué sucede con la copia de listas?")
list1=[1,2,3,4]
list2=list1
print("List1: ", list1)
print("Lis2: ", list2)

#List1 y List2 están apuntando a la misma lista
list1.append(5)
print("List1:", list1)
print("List2:", list2)

print("\n\n Cuando queramos hacer una copia en la que el puntero sea diferente:")
list3=list2.copy()
list3.append(6)
print("List2: ", list2)
print("List3:" , list3)

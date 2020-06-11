# Tipo tupla

#    Una tupla es una lista inmutable. Una tupla no puede 
#    modificarse de ningún modo después de su creación.

#Veamos un ejemplo de creación de variables con las vocales
vocales_lista = ['a', 'e','i','o','u']
print(vocales_lista, type(vocales_lista))

print("\n Ahora usaremos una tupla para guardar la misma información")
vocales_tupla = ('a','e','i','o','u')
print(vocales_tupla, type(vocales_tupla))

#La diferencia es que la tupla usa () y las listas []
#Las listas podemos cambiar un valor y las tuplas no podemos modificar 
#vocales_tupla[2]='E' #Esta línea daría un error

print("\nOJO CON EL SIGUIENTE EJEMPLO")
t=('Python')
print(t, type(t)) #¿Por que no es una tupla?

# CUIDADO cuando creemos una tupla con un elemento debe terminar en , sino Python no lo interpreta como tupla
t2=("Python", )
print(t2, type(t2))



# Ejemplo simple de tupla
tupla = 12345, 54321, 'hola!'
print(tupla, type(tupla))
# Ejemplo de tuplas anidadas
otra = tupla, (1, 2, 3, 4, 5)
print(otra)
# operación asignación de valores de una tupla en variables
x, y, z = tupla
print(x)
print(y)
print(z)



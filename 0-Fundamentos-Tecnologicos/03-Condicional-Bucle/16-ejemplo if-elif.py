# Clase: Estructuras de control selectiva
# Ejemplo de if-elif[else]
# Pedir dos números al usuario e indicar qué número es mayor que otro o si son iguales
numero1 = int(input ("Escribe un número: "))
numero2 = int(input ("Escribe otro número: "))

if (numero1 > numero2):
    print (numero1, " es mayor a ", numero2)
elif (numero2 > numero1):
    print (numero2, " es mayor a ", numero1)
else:
    print (numero1, " es igual a ", numero2)
    
print("Fin")

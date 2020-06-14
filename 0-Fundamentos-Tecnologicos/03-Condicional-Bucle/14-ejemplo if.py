#Clase: Estructuras selectivas
# Ejemplo de un if sencillo. Solo se ejecutará un código si se cumple la condición
# Pedir un número al usuario y si es negativo mostrarle el valor absoluto

num = int(input('Escribe un numero: '))
if (num < 0):
    print ('El valor absoluto del numero ', num,  ' es ', num * (-1))
print("Fin")
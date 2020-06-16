#Clase: estructuras control repetitivas. Bucle while


#Ejemplo: cuenta atras de 10 para el despegue
n=10
while n>0:
    print(n)
    n=n-1
print("¡¡Despegue!!")

#Ejemplo: pedir números al usuario hasta que sea par
num = int(input("Escribe un numero: "))
while (num%2!=0):
    num = int(input("Escribe un numero: "))
print("Gracias por tu colaboración")
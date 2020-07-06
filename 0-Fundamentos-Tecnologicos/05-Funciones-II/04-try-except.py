# Uso de excepciones
# Programa que realiza operaciones básicas +, -, *, / de dos números

def printMenu():
    print ("---*** Menú ***----")
    print("\t1 suma")
    print("\t2 resta")
    print("\t3 divide")
    print("\t4 multiplica")
    

def pideOperandos():
    while True:
        try:
            op1=int(input("Escribe nº 1: "))
            op2=int(input("Escribe nº 2: "))           
            break
        except ValueError:
            print("Datos no válidos. Solo números")
    return op1, op2
               

def suma (a,b):
    return a+b

def resta (a,b):
    return a-b

def multiplica (a,b):
    return a*b

def divide (a,b):
    try:
        operacion= a/b
    except ZeroDivisionError:
        print("No es posible dividir un número 0")
        return -1
    else:
        return operacion

def menu ():
    op=-1
    while op not in range (1,5): #op<1 or op>4
        op=int(input("\nSelecciona de 1 a 4 la operación que deseas:"))
    return op
    
def opera():
    printMenu()
    op1, op2 = pideOperandos()
    operacion=menu()
    if operacion==1:
        print("La suma de", op1, "y ", op2, " es ", suma(op1,op2))
    elif operacion==2:
        print("La resta de", op1, "y ", op2, " es ", resta(op1,op2))
    elif operacion==3:
        if divide(op1, op2)!=-1: 
            print("La división de", op1, "y ", op2, " es ", divide(op1,op2))
    elif operacion==4:
        print("La multiplicación de", op1, "y ", op2, " es ", multiplica(op1,op2))
    else:
        print("Operación no realizada")



if __name__ == "__main__":
    opera()

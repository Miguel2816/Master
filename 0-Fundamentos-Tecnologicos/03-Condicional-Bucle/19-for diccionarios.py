#Diccionarios y for

#Esccribir una frase e indicar cuantas veces se repiten las vocales

#Declaramos un diccionario vocales_encontradas
vocales=('a','e','i','o','u')
vocales_encontradas={
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}
frase = input("Frase")
for vocal in frase:
    if vocal in vocales:
        vocales_encontradas[vocal]=vocales_encontradas[vocal]+1

for clave, valor in vocales_encontradas.items():
    print(clave, "ha sido encontrada ", valor, " veces")


#Ejemplo reiniciar stock a cero. Como se usa setdefault
#Ejemplo de diccionario que tiene el stock de productos
dicc_stock={
    'peras':45,
    'manzanas': 90,
    'melones': 30,
    'plátanos': 20
}
print("Actualmente el stock es: ", dicc_stock)
#Se vacia el stock y hay que reiniciar a un valor: 0
for clave, valor in dicc_stock.items():
    dicc_stock[clave]=0

print("Despues de vender todo el stock ha quedado vacío ", dicc_stock)
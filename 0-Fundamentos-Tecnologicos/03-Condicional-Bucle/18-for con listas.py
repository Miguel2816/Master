# Listas-For

#¿Qué vocales tiene una palabra pedida al usuario?
vocales = ['a', 'e', 'i', 'o', 'u']
palabra=input("Palabra: ")
print("La palabra ", palabra, "tiene las siguientes vocales:")
for vocal in palabra:
    if vocal in vocales:
        print(vocal)

#A continuación se debe hacer lo mismo pero se deberá
#guardar en una lista las vocales encontradas por si más adelante se necesitan
palabra=input("Palabra: ")
encontradas =[] #Creamos una lista vacía
print("La palabra ", palabra, "tiene las siguientes vocales:")
for vocal in palabra:
    if vocal in vocales:
        encontradas.append(vocal)
        print(vocal)

print("Las vocales encontradas son ", encontradas)

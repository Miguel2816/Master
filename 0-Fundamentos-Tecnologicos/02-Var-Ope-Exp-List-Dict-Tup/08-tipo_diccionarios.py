# Tipo diccionarios
# Conjunto de datos desordenados tipo clave:valor
# Permite distinto tipo
# Mutables
# Se crean con  { } poniendo su clave:valor separdos por comas 


print("\nEjemplo de un diccionario países y capitales donde se usa cadenas como clave y valor")
midiccionario={
    "Alemania" : "Madrid",
    "Francia": "París",
    "Reino Unido" : "Londres",
    "España": "Madrid"
}

print(midiccionario)

print("\nAccedemos con [key]")
print(midiccionario["Alemania"])

print("\nAñadimos un nuevo elemento")
midiccionario["Italia"] = "Lisboa" #estamos poniendo aposta mal el valor para luego cambiarlo
print(midiccionario)

print("\nModificamos un valor: ")
midiccionario["Italia"] = "Roma" #sobreescribe el valor de Lisboa y guarda Roma porque 
                                #una clave solo puede tener un valor
print(midiccionario)

print("\nEliminar un elemento con método del ")
del midiccionario["Reino Unido"] #eliminará la clave-valor de Reino Unido
print(midiccionario)


pais=input("\nEScribe un pais para comprobar si está en diccionario: ")
if pais in midiccionario:
    print(pais, " pertenece al diccionario")
else:
    print(pais, " no está en el diccionario")

#Ejemplo
#Ahora vamos a crear un diccionario con una tupla y cadenas. 

mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario={
    mitupla[0]: "Madrid", #con mitupla[posicion] accedemos al pais de la tupla
    mitupla[1]: "París",
    mitupla[2]: "Londres",
    mitupla[3]: "Berlín"

}
print(midiccionario)
print(midiccionario["Francia"])

#Ejemplo
#Un diccionario alamacene en su interior con otros valores una tupla

midiccionario = {
    23:"Jordan",
    "Nombre": "Michael",
    "Equipo": "Chicago",
    "Anillos": [1991, 1992, 1993, 1996, 1997, 1998]#creamos una tupla con los anillos para alamacenar años que ganó anillos
}
print(midiccionario)
print(midiccionario["Equipo"])
print(midiccionario["Anillos"])

#Ejemplo guardar un diccionario dentro de otro, donde el segundo diccionario tiene una tupla
midiccionario = {
    23:"Jordan",
    "Nombre": "Michael",
    "Equipo": "Chicago",
    "Anillos": {
        "Temporadas": [1991, 1992, 1993, 1996, 1997, 1998]
        #creamos una tupla con los anillos para alamacenar años que ganó anillos
    }
}

print(midiccionario)

#Algunos metodos interesantes para los diccionarios
print(midiccionario.keys()) #devuelve las claves del diccionario
print(midiccionario.values()) #devuelve los valores
print(len(midiccionario)) #longitud de mi diccionario


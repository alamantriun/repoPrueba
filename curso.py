#Metodos
"""
cadena1 = "Hola Mundo"
resultado = cadena1.capitalize() #convierte la primera letra en mayuscula y el resto en minuscula

print(resultado)

print(cadena1.upper()) #convierte a mayusculas
print(cadena1.lower()) #convierte a minusculas
print(cadena1.replace("Mundo", "Python")) #reemplaza una palabra por otra

###//metodo// = variable.metodo()

cadena_busqueda = cadena1.find("Mundo") #busca la palabra y devuelve su posicion
print(cadena_busqueda)#si no la encuentra devuelve -1

###chismosear si es numeroco o no
cadena2 = "12345"
print(cadena2.isnumeric()) #devuelve True si es numerico, False si no

##metodo split() divide una cadena en una lista de palabras
cadena3 = "Hola Mundo"
print(cadena3.split()) #devuelve una lista de palabras

##fijarse si una variable tiene caracteres alfanumericos o no
cadena4 = "Hola123"
print(cadena4.isalnum()) #devuelve True si es alfanumerico, False si no

##contar contar cuantas veces aparece una palabra en una cadena
cadena5 = "Hola Mundo Hola"
print(cadena5.count("Hola")) #devuelve el numero de veces que aparece la palabra

##cuantos caracteres tiene una cadena
cadena6 = "Hola Mundo"
print(len(cadena6)) #devuelve el numero de caracteres de la cadena

##verificar si una cadena empieza o termina con una palabra
cadena7 = "Hola Mundo"
print(cadena7.startswith("Hola")) #devuelve True si empieza con la palabra, False si no
print(cadena7.endswith("Mundo")) #devuelve True si termina con la palabra, False si no

###remplazar caracteres especiales por espacios
cadena8 = "Hola-Mundo"
print(cadena8.replace("-", " ")) #reemplaza el guion por un espacio
"""
"""
                    ###METODOS DE LISTAS###

#convierte una cadena en una lista de caracteres
lista = list(("hola", "dato", "python"))
print(lista)

#agrega un elemento al final de la lista
lista.append("nuevo dato")
print(lista)

#devuelve cantidad de elemtos de una lista
print(len(lista))

#agrega varios elementos a la lista
lista.extend(["otro dato", "mas dato"]) 
print(lista)

lista.insert(1, "dato insertado") #inserta un elemento en una posicion especifica
print(lista)

lista.pop(2) #elimina un elemento de la lista por su posicion
print(lista)


lista.pop(-1) #elimina el ultimo elemento de la lista
print(lista)

#remueve un elemento de la lista por su valor
lista.remove("dato insertado") ##si lo encuentra lo elimina, si no lo encuentra devuelve un error   
print(lista)

#ordena una lista de menor a mayor 
lista.sort()
print(lista)

"""
            ##metodos de diccionarios

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

#devuelve las claves del diccionario
print(diccionario.keys())

#devuelve los valores del diccionario
print(diccionario.values())

#devuelve los pares clave-valor del diccionario
print(diccionario.items())

#dame un valor clave del diccionario ()si la clave no existe devuelve un valor por defecto
print(diccionario.get("nombre")) #devuelve el valor de la clave "nombre"








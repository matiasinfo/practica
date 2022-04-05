import string 
""" la manera de resolverlo fue: creando un conjunto, usando una lista, que contiene las letras de la palabra
    o frase que es ingresada por teclado """

minusculas = string.ascii_lowercase
frase = input("ingrese una frase o palabra: ").lower()
lista = [elem for elem in frase if elem in minusculas]
heterograma = set(lista)
print( f" {frase}: SI es un heterograma " if len(heterograma)== len(lista) else f"{frase}: NO es un heterograma")

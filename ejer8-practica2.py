import string
def crear_tabla():
    puntos = [("A","E","I","O","U","L","N","S","T",1),
              ("D","G",2),
              ("B","C","M","P",3),
              ("F","H","V","W","Y",4),
              ("K",5),
              ("J","X",8),
              ("Q","Z",10)]
    tabla_valores = dict([(n,0)for n in string.ascii_uppercase])
    for tupla in puntos: 
        for letra in tupla:
            if letra in tabla_valores:
                tabla_valores[letra] = tupla[-1]
    return tabla_valores

def evaluo(palabra,tabla):
    total = 0
    for letra in palabra:
        total += tabla[letra]
    return total

def cumple(palabra,letras):
    ok = True
    cant = 0
    while ok and cant < len(palabra):
        if not palabra[cant] in letras:
            ok = False
        cant += 1
    return ok

tabla = crear_tabla()
abecedario = string.ascii_uppercase
palabra = input(" ingrese una palabra: ").upper()
if cumple(palabra,abecedario):
    print(f" los puntos que suman la palabra: {palabra} son: {evaluo(palabra,tabla)}")
else:
    print("OPS algun caracter ingresado no era una letra..")
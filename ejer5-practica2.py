frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres.".lower().split(",").split(" ").split(".").split()
palabra = "tigres"
cant = 0
for elem in frase:
    print(elem)
    if elem == palabra:
        cant += 1
print (cant)




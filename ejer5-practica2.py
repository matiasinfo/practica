frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres.".lower().replace(",","").replace(".","").split()
palabra = "tres"
cant = 0
for elem in frase:
    print(elem)
    if elem.replace(",","").lower() == palabra:
        cant += 1
print (cant)




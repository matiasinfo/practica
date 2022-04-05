cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !): ")
cumple = len(cadena)<10 and not ("@" and "!") in cadena
print("Clave válida" if cumple else "la clave no cumple con lo solicitado")


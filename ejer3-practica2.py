import string
letras_minus = string.ascii_lowercase
texto = """Para el acceso al material tendremos un sitio web alternativo para que puedan consultar.
1- Realizar la instalación de Python 3.X. recomendado 3.10
Para esta actividad existen 3 alternativas: * Instalar python en forma local, para windows seguir
esta guía. * Utilizar una herramienta para realizar la instalación en tu sistema operativo: Conda
o Pyenv. Para conocer un poco más qué son los entornos virtuales puede consultar esta guía *
Utilizar directamente la Máquina Virtual provista por la cátedra. Para esto es necesario que se
instale en el sistema operativo una herramienta de virtualización como VirtualBox.
2- Escriba en un archivo llamado adivino.py el siguiente programa en Python (similar al que
vieron en la teoría Clase 1 de la teoría)."""

texto1 = texto.lower().split(" ")
caracter = input("ingrese una letra del abecedario , no un caracter: ").lower()
if caracter in letras_minus:
    for elem in texto1:
        if elem.startswith(caracter):
            print(elem)
else: print(" el caracter ingesado no es una letra")
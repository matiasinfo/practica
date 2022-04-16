import os
import csv

def abrir_archivos():
    base_path = os.path.abspath(os.path.dirname(__file__))
    archi_evaluacion1 = f'{base_path}\\archivo\eval1.txt'
    archi_evaluacion2 = f'{base_path}\\archivo\eval2.txt'
    archivo_nombres = f'{base_path}\\archivo\\nombres_1.txt'

    with open(archi_evaluacion1,'r') as puntero1:
        notas1 = puntero1.read()
    with open(archi_evaluacion2,'r') as puntero2:
        notas2 = puntero2.read()
    with open (archivo_nombres,encoding="utf8") as puntero3: 
        nombres = puntero3.read() 
    return(notas1,notas2,nombres)

def extraer_info(info):
    lista = info.split(",")
    nueva = list(map(lambda elem : int(elem.replace(" ","")),lista))
    return nueva

def extraer_nombres(nombres):
    lis_nombres = nombres.split(",")
    nom = list(map(lambda elem : elem.replace(" ","").replace("\n","").replace("'",""),lis_nombres))
    return nom

def agrupo_info(notas1,notas2,nombres_limpios):
    ficha_datos = []
    indice = 0
    total = 0
    for elem in nombres_limpios:
        suma = notas1[indice] + notas2[indice]
        alumno = [elem,notas1[indice],notas2[indice],suma]
        total += suma
        ficha_datos.append(alumno)
        indice += 1
    return (ficha_datos,total)
def main():
    notas1,notas2,nombres = abrir_archivos()
    evaluacion_1 = extraer_info(notas1)
    evaluacion_2 = extraer_info(notas2)
    nombres_limpios = extraer_nombres(nombres)
    datos_alumnos,total = agrupo_info(evaluacion_1,evaluacion_2,nombres_limpios)

    if len(datos_alumnos) >0:
        promedio = total / len(datos_alumnos)
    for elem in datos_alumnos:
        if elem[3] < promedio:
            print (f'{elem[0]:10}  de nota: {elem[3]} ,')
    print (f" estos son los alumnos los cuales sus notas estan por debajo del promedio que es: {promedio} ")

if __name__ == '__main__':
    main()
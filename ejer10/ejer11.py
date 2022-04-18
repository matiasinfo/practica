from ejer10 import extraer_nombres
from ejer10 import extraer_info
import os

def abrir_archivos():
    
    base_path = os.path.abspath(os.path.dirname(__file__))
    separador = os.sep
    archivo_nombres1 = f'{base_path}{separador}archivo{separador}nombres_1.txt'
    archivo_nombres2 = f'{base_path}{separador}archivo{separador}nombres_2.txt'
    archi_evaluacion1 = f'{base_path}{separador}archivo{separador}eval1.txt'
    archi_evaluacion2 = f'{base_path}{separador}archivo{separador}eval2.txt'
    with open(archi_evaluacion1,'r') as puntero1:
        notas1 = puntero1.read()
    with open(archi_evaluacion2,'r') as puntero2:
        notas2 = puntero2.read()
    with open (archivo_nombres1,encoding="utf8") as puntero1: 
        nombres1 = puntero1.read()
    with open (archivo_nombres2,encoding="utf8") as puntero2: 
        nombres2 = puntero2.read()
    
    return (notas1,notas2,nombres1,nombres2)  
    
              
def limpiar_datos(nombres1,nombres2,notas1,notas2):
    nombres1_limpios = extraer_nombres(nombres1)
    nombres2_limpios = extraer_nombres(nombres2)
    notas1_limpias = extraer_info(notas1)
    notas2_limpias = extraer_info(notas2)
    
    return(nombres1_limpios,nombres2_limpios,notas1_limpias,notas2_limpias)


def main():
    notas1,notas2,nombres1,nombres2 = abrir_archivos()
    nom1,nom2,not1,not2 = limpiar_datos(nombres1,nombres2,notas1,notas2)
    nombres_repetidos = set([elem  for elem in nom1 if elem in nom1 and elem in nom2])
    print(f'estos son los nombres que aparecen en ambas listas : {nombres_repetidos}')
    i = 0
    print(f'{"    Nombre":15}      {"Eval1":10}  {"Eval2":10} {"Total":10}')
    for elem in nom1:
        print(f'{i:3}  {elem:10} {not1[i]:10}{not2[i]:10}   {not1[i] + not2[i]:10}')
        i += 1

if __name__ =='__main__':
    main()
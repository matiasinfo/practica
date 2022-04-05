from posixpath import split

evaluar = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python.
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

def creo_dici ():
    dicci = {"facil": 0, "aceptable": 0, "dificil": 0, "muy_dificil": 0}
    return dicci


def evaluar_titulo (texto):
    """ este metodo evalua la cantidad de palabras que contiene el titulo """
    oraciones = texto.split(".")
    print(oraciones[0])
    if "título:" in oraciones[0][0:8]:
        titulo = oraciones[0].split()[1:]
        print ("titulo esta ok "if len(titulo) <= 10 else " el titulo no cumple contiene ")
    
        #que pasa si no esta la palabra "titulo: en el string" ?
    
    return (oraciones[1:])

def evaluar_resumen(categorias, texto):
    
    if "resumen:" in texto[0]:
        texto[0] = texto[0][8:] 
        for elem in texto:
            cant = len(elem.split())
            if cant <= 12:
                categorias["facil"]+= 1
            elif cant <= 17:
                categorias["aceptable"]+= 1
            elif cant <= 25:
                categorias["dificil"]+= 1
            else:
                categorias["muy_dificil"]+= 1

        
categorias = creo_dici()

resumen = evaluar_titulo(evaluar)

evaluar_resumen(categorias, resumen)
print (categorias)


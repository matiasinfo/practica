frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""
def limpiar(texto):
    """ descompone el texto y la retorna en una lista que contiene las palabras del texto"""
    nueva = []
    if len(texto) > 0:
        for elem in frase.lower().split(","):
            for elem in elem.split("."):
                for palabra in elem.split():
                    nueva.append(palabra)
    return nueva
                        
sin_repetir = list(set(limpiar(frase)))
print(len(sin_repetir))
print(sin_repetir)
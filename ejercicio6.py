import string
frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""

frase = frase.lower().split()   #frase pasa de ser de tipo Literal(str) a una List de str(cada palabra) en minuscula
frase = set([''.join(char for char in stri if char not in string.punctuation) for stri in frase])   #solo deja en las palabras(stri) los caracteres(char) que no son signos de puntuacion, como , o . (string.punctuation), y estas palabras las guarda en la lsta frase que luego se convierte en set con set()

for palabra in frase:
    print(palabra)
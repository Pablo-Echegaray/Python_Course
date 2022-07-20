import os
# getcwd() : nos devuelve el directorio de trabajo actual
# ruta = os.getcwd()
# chdir() : nos permite cambiar de directorio
# ruta = os.chdir('C:\\Users\\Voolkia\\Desktop\\Alternativo')
# ya que nuestro directorio ahora es el indicado en la linea 5
#archivo = open('otro_archivo.txt')
#print(archivo)
# makedirs : nos permite crear directorios
# ruta = os.makedirs('C:\\Users\\Voolkia\\Desktop\\Alternativo\\otra')

# Separar la directorio de archivo :

ruta = 'C:\\Users\\Voolkia\\Desktop\\Python\\Dia6\\prueba.txt'

elemento = os.path.basename(ruta) # archivo
directorio = os.path.dirname(ruta) # directorio
elem_direc = os.path.split(ruta) # tuple con ambos
print(elemento) # prueba.txt
print(directorio) # C:\\Users\\Voolkia\\Desktop\\Python\\Dia6
print(elem_direc) # ('C:\\Users\\Voolkia\\Desktop\\Python\\Dia6', 'prueba.txt')

# Eliminar una carpeta :
os.rmdir('C:\\Users\\Voolkia\\Desktop\\Alternativo\\otra')

# Abrir archivos alojados en un directorio distinto al actual
otro_archivo = open('C:\\Users\\Voolkia\\Desktop\\Alternativo\\otro_archivo.txt')
print(otro_archivo.read())

# Crear rutas que puedan ser interpretadas independientemente del sistema operativo
from pathlib import Path

# Al haber creado la ruta a partir de Path, cualquier os puede interpretarlo
# Podemos incluso obviar "C:" en la ruta (como en mac) y funcionara igual
carpeta = Path('/Users/Voolkia/Desktop/Alternativo')
# con "/" concatenamos a una ruta
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())
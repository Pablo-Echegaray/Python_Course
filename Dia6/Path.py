from pathlib import Path

base = Path.home() # nos brinda el directorio base del usuario
# guia = Path("Barcelona", "sagrada_familia.txt") # crea rutas relativas con los strings que le pasemos.
# guia = Path(base, "Barcelona", "sagrada_familia.txt") # concatenamos nuestro home a la ruta relativa = ruta absoluta.
guia = Path(base, "Europa", "España", Path("Barcelona", "sagrada_familia.txt")) # concatena y crea la ruta sin problemas.
guia2 = guia.with_name("la_pedrera.txt") # replicamos la ruta anterios pero cambiando el archivo de destino
print(guia) #C:\Users\Voolkia\Europa\España\Barcelona\sagrada_familia.txt
print(guia2) #C:\Users\Voolkia\Europa\España\Barcelona\la_pedrera.txt

print(guia.parent) # Devuelve la ruta hasta el ancestro mas cercano : C:\Users\Voolkia\Europa\España\Barcelona\
print(guia.parent.parent) # C:\Users\Voolkia\Europa\España\

# Enumerar archivos en carpetas (para este ejercicio no tenemos las carpetas creadas, se deberian crear a partir del home)
guia3 = Path(Path.home(),"Europa")

for txt in Path(guia3).glob("*.txt"):
    print(txt) # Imprimimos al txt que se encuentre en cada iteracion
#Este for enumerara solo los archivos .txt que esten en la carpeta europa
# Pero podemos crear una iteracion de forma recursiva que muestra todos los .txt
# de los subdirectorios tambien.

for txt in Path(guia3).glob("**/*.txt"):
    print(txt)

# "**/*.txt" : esto hace que incluya todas las carpetas y subcarpetas que vaya encontrando
# hasta llegar a enumerar todos los .txt dentro de Europa.

# Tambien podemos calcular rutas relacionadas entre si.
# relative_to() : es muy util cuando se desea recuperar una porcion de una ruta de archivos larga.
# devuelve un nuevo objeto Path relacionado con el argumento determinado.

guia4 = Path("Europa", "España", "Barcelona", "sagrada_familia.txt")
# Construir rutas que vayan de alguno de estos puntos hacia abajo
en_europa = guia4.relative_to(Path("Europa"))
en_espania = guia4.relative_to(Path("Europa", "España"))

print(en_europa) # España\Barcelona\sagrada_familia.txt
print(en_espania) # Barcelona\sagrada_familia.txt
# De esta manera podemos construir rutas que nos permitan ver el contenido
# de carpetas especificas.


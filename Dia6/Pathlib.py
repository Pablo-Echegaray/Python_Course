from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/Voolkia/Desktop/Python/Dia6/prueba.txt')
# read_text() = read() : utilizando el modulo Path no necesitamos hacer un open()
# primero para poder leer un archivo
print(carpeta.read_text())
print(carpeta.name) # nombre de archivo (prueba.txt)
print(carpeta.suffix) # terminacion (.txt)
print(carpeta.stem) # nombre sin terminacion (prueba)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")

# PureWindowsPath : transforma cualquier ruta en una ruta de windows.
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows) # C:\Users\Voolkia\Desktop\Python\Dia6\prueba.txt

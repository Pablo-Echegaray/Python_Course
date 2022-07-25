def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")

try:
    # Codigo a probar
    suma()
except TypeError:
    # Codigo a ejecutar si hay un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    # Codigo a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    # Codigo que se va a ejecutar de todos modos
    print("Eso fue todo")

# pylint : nos permite verificar errores de nuestro codigo
# Desde la terminal lo instalamos : C:\users\win10> pip install pylint
# Navegamos hacia donde se encuentra el archivo que queremos testear
# Ejecutamos > pylint archivo.py -r y
# -r : reporte, y = yes
# pylint es mas que nada una herramienta para trabajar en equipo.
# pylint nos dara un puntaje en base a si cumplimos con la mayoria de las convenciones al momento de escribir codigo.
# por convencion al comenzar cada archivo nuevo de py debe haber un comentario que explique brevemente
# lo que hace el codigo con un comentario de varias lineas. Y espacios de dos lineas entre cada sentencia.
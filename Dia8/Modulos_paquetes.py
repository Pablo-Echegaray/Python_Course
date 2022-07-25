# Se denomina MODULO a cualquier archivo guardado con extension ".py".
# Un modulo puede alvergar un conjunto de funciones, variables y clases, y tambien puede ser usado por otros modulos.
# Paquetes : Son colecciones de modulos. Un paquete es una carpeta que contiene varios modulos.
# __init__.py : Es un modulo especial que debe existir al interior de cada paquete y a la misma altura, que nuestros otros modulos.
# Todo paquete debe contener siempre un modulo especial para que python entienda que se trata de un paquete y no de
# una simple carpeta. Incluso podemos crear subpaquetes dentro de los paquetes, pero cada uno de ellos
# tambien debera contener un __init__.py para indicarle a python que se trata de un conjunto de modulos empaquetados.
# De esa manera la importacion de puede hacer llamando al paquete e importando sus modulos.
# from Paquete import modulo

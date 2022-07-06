# Las tuples a diferencia de las listas son inmutables como los Strings.
# Una vez que un elemento fue asignado a un tuple, no puede cambiarse ni reasignarse.
# Los tuples ocupan menos espacio de memoria, por lo tanto se procesan mas rapido
# Las usariamos para almacenar estructuras que no quisieramos que sean modificadas (a prueba de danios).

mi_tuple = (1,2,3,4)
# Podemos tambien obviar los parentesis
# mi_tuple = 1,2,3,4

# Los tuples pueden contener objetos de distintos valores.
t = (5,5.6,"Hola")
print(type(mi_tuple))
print(mi_tuple[0]) # 1
print(mi_tuple[-2]) # 3

mi_tuple2 = (1,2,(10,20),4)
print(mi_tuple2[2][0]) # 10

# Se puede hacer casting
# Convertimos un tuple en una lista
mi_tuple = list(mi_tuple)
print(type(mi_tuple)) # tuple
# Y volver a castearlo a tuple
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

# Desempaque de valores
# Es importante que la cantidad de variables a crear coincida con la cantidad de valores que contiene el tuple
# Sino nos arrojara error
tpl = (1,2,3)

x,y,z = tpl

print(x,y,z) # x = 1, y = 2, z = 3

# conunt() -> cuenta la cantidad de apariciones de un elemento dentro del tuple
tpl2 = (1,2,3,1)
print(tpl2.count(1)) #2
print(tpl2.index(2)) #1 -> Nos indica el indice donde se encuentra.

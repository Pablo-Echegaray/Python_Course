# RANGE ---> RANGO
#Funcion Rango -> Range. Comienza en 0 hasta donde le indiquemos sin incluir el numero que le indicamos
# range(desde, hasta) -> range(1,5)
# range(desde, hasta, deACuantosSaltar) -> range(20,31,2) -> 20,22,24,26,28,30

for numero in range(5):
    print(numero) # 0,1,2,3,4

#Tambien podemos usar el rango para crear listas que sean de varios numero consecutivos
lista = list(range(1,101)) #Nos crea una lista con numeros del 1 al 100 (el 101 no se incluye.

print(lista)

#-------------------------------------------------------------------
# ENUMERATE : Su funcion es hacernos la vida mas facil cuando necesitamos acceder a los indices de una coleccion.

lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

#-----------------------------------------
# Con Enumerate
for item in enumerate(lista):
    print(item) # (0, 'a') (1, 'b') (2, 'c')
    #enumerate posee una serie de tuples que contienen al indice y al elemento

#Para imprimir el indice y el item por separado :
for indice, item in enumerate(lista):
    print(indice, item) #0 a, 1 b, 2 c

#-----------------------------------------
#Utilizar enumerate para converir una lista de strings, en una lista de tuples.
mis_tuples = list(enumerate(lista))
print(mis_tuples)#[(0, 'a'), (1, 'b'), (2, 'c')]
print(mis_tuples[1][0])# 1

#Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los indices
#de cada caracter mediante enumerate() los indices de cada caracter del string "Python".
#Llama a la lista obtenida con el nombre de variable lista_indices.

var = "Python"
mi_tuple = enumerate(var)
print(mi_tuple)
lista_indices = list(mi_tuple)
print(lista_indices)

#-----------------------------------------------------------------------------------------
# ---> ZIP : Combina 2 o mas listas entrelazando sus elementos en tuples.
nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(nombres, edades))
print(combinados) #[('Ana', 65), ('Hugo', 29), ('Valeria', 42)]
#Por caso si tuvieramos un elemento de mas en cualquiera de las dos listas, lo que hace zip es llegar al largo
#de la lista mas corta, por lo tanto simplemente zip no tendria en cuenta ese elemento de mas.

combinados2 = list(zip(nombres, edades, ciudades))
print(combinados2) #[('Ana', 65, 'Lima'), ('Hugo', 29, 'Madrid'), ('Valeria', 42, 'Mexico')]

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")

#----------------------------------
espaniol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espaniol, portugues, ingles))





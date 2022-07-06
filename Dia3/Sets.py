# Los Sets en python son una coleccion de elementos al igual que las listaas
# Se pueden declarar de dos formas diferentes :
# Usando la palabra set(1,2,3,4,5,6) o directamente con llaves {1,2,3,4,5,6}
# Si creamos el set con la palabra reservada set() nuestros elementos deben estar encerrados
# en corchetes, llaves, o incluso otro par de parentesis para que pyhton lo identifique como un unico argumento set([1,2,3,4,5])
# ya que los sets solo admiten un unico argumento
# Los sets solo admiten elementos unicos, no se pueden repetir valores.
# Si se agregan elementos duplicados, python simplemente los descarta sin preguntar y deja los valores unicos.
# Al igual que los diccionarios, sus elementos no estan ordenados en indices, por lo tanto no se puede indexar
# sus elementos ni ordenarlos.
# Sus elementos son inmutables, y no se pueden incluir dentro de los sets listas ni diccionarios.

mi_set = set((1,2,3,4,5))
print(type(mi_set)) # class set
print(mi_set) # {1,2,3,4,5}

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

otro_set2 = {1,2,3,4,5,1,1,1,2,2,2}
print(otro_set2) # {1,2,3,4,5}

# Los sets no admiten listas ni diccionarios como valores internos
# Pero si tuples, ya que estos son inmutables y no estan ordenados.

otro_set3 = {1,2,3,4,(1,2,3),5,6}
print(otro_set3) # {1,2,3,4,(1,2,3),5,6}
print(len(otro_set3)) # 7
print( 2 in otro_set3) # True

# Union de sets
s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1.union(s2)

print(s3) # {1,2,3,4,5}

# Podemos agregar elementos a nuestro set con add()
# Si agregamos un elemento que ya existe en el set simplemente no lo agregara
s1.add(4)
print(s1) # {1,2,3,4}

#Podemos eliminar elementos de un set con remove()
s1.remove(3)
print(s1) # {1,2,4}
# Si el indicamos que elimine un elemento que no existe, nos arrojara error

# discard() -> funciona igual que remove() con la diferencia que si le pedimos descartar un elemento
# inexistente, simplemente no lo hara pero no arrojara error

# Como los sets no tienen un orden, pop() eliminara un elemento aleatorio
sorteo = s1.pop()

print(sorteo) # elemento aleatorio

# clear() vacia nuestro set
s1.clear()
print(s1) # {}
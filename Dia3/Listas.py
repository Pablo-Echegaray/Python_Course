#Las listas si son mutables a diferencia de los strings
#Pueden estar compuestas por diferentes tipos de datos

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
otra_lista = ['a', 3, 2.3, False]

resultado = len(mi_lista)
resultado2 = mi_lista[0 : ] #Mismos metodos que con los strings
print(otra_lista)
print(resultado)
print(type(mi_lista))
print(mi_lista + mi_lista2) # ['a', 'b', 'c','d', 'e', 'f']

#Alteramos elementos de una lista

otra_lista[0] = 'alfa' #['alfa', 3, 2.3, False]

print(otra_lista)

otra_lista.append('g') #['alfa', 3, 2.3, False, 'g']
#Esto no es una concatenacion, es agregar un elemento nuevo a la lista ya existente
print(otra_lista)

otra_lista.pop() #pop() sin parametros elimina el ultimo elemento de la lista

print(otra_lista)

otra_lista.pop(0) #Elimina el primer elemento de la lista

print(otra_lista)

#Podemos almacenar en una variable el elemento eliminado
eliminado = mi_lista.pop(0) #'a'
print(eliminado)

#Ordenar una Lista
#sort() -> no tiene valor de retorno
lista = ['g','o','b','m','c']
lista.sort() #Ordena alfabeticamente la lista en el caso de letras
print(lista)

nueva_lista = lista.sort() #None
print(type(nueva_lista)) #NoneType : es el tipo de dato de un no objeto. Un objeto que no tiene valor.

#Inversion del orden
lista.reverse() #orden alfabetico invertido, de la z a la a
print(lista) #['o', 'm', 'g', 'c', 'b']

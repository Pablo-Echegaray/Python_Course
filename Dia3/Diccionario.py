# { 'clave' : 'valor'}
# Las claves deben ser unicas
# No tienen un orden
# No se puede buscar valores en funcion de su indice, sino a traves de la clave
# Una buena situacion para usar diccionario es cuando queremos acceder a un valor sin conocer su ubicacion exacta
# sino a traves de su clave.
# Los valores si pueden repetirse a diferencia de las claves
#Al igual que las listas podemos modificar un elemento ya existente

diccionario = {'c1':'valor1', 'c2':'valor2'}

print(type(diccionario)) #dict
print(diccionario) #{'c1':'valor1', 'c2':'valor2'}

resultado = diccionario['c1']
print(resultado) #valor1

cliente = {'nombre' : 'Juan', 'apellido' : 'Fuentes', 'peso' : 88, 'talla' : 1.76}

consulta = (cliente['apellido'])
print(consulta) #'Fuentes'

dic = {'c1' : 55, 'c2' : [10,20,30], 'c3' : {'s1':100, 's2': 200}}

print(dic['c2'][1]) #20
print(dic['c3']['s2']) # 200

dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}

print(dic2['c2'][1].upper()) #E

#Agregar elementos a un diccionario ya existente
dic3 = {1:'a', 2:'b'}
print(dic3)
dic3[3] = 'c' #Agregamos una nueva clave 3 con valor 'c'
print(dic3) #{1:'a', 2:'b', 3:'c'}

#Sobrescribir un valor
dic3[2] = 'B'

print(dic3) #{1:'a', 2:'b', 3:'B'}

print(dic3.keys()) #Nos trae todas las claves(llaves) {1, 2, 3}
print(dic3.values()) #Nos trae todos los valores {'a', 'b', 'B'}
print(dic3.items()) #Nos trae todos los elementos del diccionario
#dic_items{(1:'a'), (2:'b'), (3:'B')} #Esto nos da la pauta de que lo que hay dentro de los diccionarios son TUPLES.

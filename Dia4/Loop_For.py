lista = ['a', 'b', 'c', 'd',]

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra} : {letra}")

#-----------------------------------------------------------------
nombres = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in nombres:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con L')

#-----------------------------------------------------------------

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor) #aqui el print esta fuera del loop, si la tabulacion estaria a la altura de 'mi_valor'
#entonces el print estaria dentro del loop.

#-----------------------------------------------------------------------
for a,b in [[1,2], [3,4], [5,6]]:
    print(a)#1 - 3 - 5
    print(b)#2 - 4 - 6
# El elemento 'a' es el primer elemento de cada sublista, y el 'b' el segundo elemento.
# Podemos iterar tambien sobre tuples

#-----------------------------------------------------------------------
# Iterar sobre un diccionario
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for item in dic:
    print(item) #Esto imprime solo las claves.

for item in dic.items():
    print(item) # ('clave1' : 'a')

for item in dic.values():
    print(item) #Esto imprime solo los valores.

for a, b in dic.items():
    print(a, b) # Esto imprime : clave valor
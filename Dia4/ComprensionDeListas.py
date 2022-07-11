palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# Podemos hacerlo de una forma mas simplificada :

lista2 = [letra for letra in palabra]
#Obtenemos el mismo resultado de una forma mas reducida. Le estamos diciendo que queremos una lista formada por letras
#de cada letra de palabra.
print(lista2)

# Podemos hacerlo sobre un rango de numeros :
lista_numerica = [n for n in range(0,21,2) if n * 2 > 10]
#Todos los numeros del 0 al 20 (inclusive) de dos en dos, si 'n' multiplicado por 2 es mayor a 10
print(lista_numerica)

# Si se agrega un else cambia la manera en como se pone el if
lista_numerica2 = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(lista_numerica2)

# Transformar una lista de medidas en pies a metros :
pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]

print(metros)
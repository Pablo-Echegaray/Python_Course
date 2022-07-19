#Crear una funcion que a partir de una lista elimine los elementos duplicados y elemento mayor.

lista_numeros = [1, 2, 15, 7, 2]


def reducir_lista(lista):
    mi_set = set(lista)
    lista_sin_duplicados = list(mi_set)
    numero_mas_alto = 0
    indice = 0
    for i,n in enumerate(lista_sin_duplicados):
        if (n > numero_mas_alto):
            numero_mas_alto = n
            indice = i
    lista_sin_duplicados.pop(indice)
    return lista_sin_duplicados
lista = reducir_lista(lista_numeros)

print(lista)

'''
def promedio(lista):
    promedio = 0

    for n in lista:
        promedio += n

    return promedio / len(lista)
'''

# Crear una funcion lanzar_moneda() que devuelva "Cara" o "Cruz". Crear una segunda funcion probar_suerte() que tome dos argumentos
# (lazamiento de la moneda, lista de numeros). Si el lanzamiento da "Cara" la lista si vacia, si da "Cruz" la lista se salva.

import random

lista_numeros = [1,2,3,4,5]

def lanzar_moneda():
    mi_tuple = ("Cara", "Cruz")
    return random.choice(mi_tuple)

def probar_suerte(lanz, lista):
    mensaje = ""
    if lanz == "Cara":
        mensaje = "La lista se autodestruirá"
        lista.clear()
    else:
        mensaje = "La lista fue salvada"
    print(mensaje)
    return lista

print(probar_suerte(lanzar_moneda(), lista_numeros))


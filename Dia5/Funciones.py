from random import shuffle

def calcularElCuadradoDeUnNumero(numero):
    return numero ** 2

resultado = calcularElCuadradoDeUnNumero(4)

print(resultado)

# Funciones Dinamicas

def chequear_3_cifras(lista):

    lista_3_cifras =[]
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n) #return True
        else:
            pass
    return lista_3_cifras #return False

resultado_chequeo = chequear_3_cifras([555,99,600])
print(resultado)

#Crear una funcion que devuelva True si todos los elementos de una lista son positivos
#y False si uno de ellos no lo es.

lista_numeros = [2,-3,4,6,7,-4]

def todos_positivos(lista):
    for n in lista:
        if n > 0:
            pass
        else:
            return False
    return True

#Funcion que despacha un Tuple
precios_cafe = [('capuchino', 1.5), ('Expreso', 1.2), ('Moka', 1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return(cafe_mas_caro,precio_mayor)

print(cafe_mas_caro(precios_cafe))

cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")

#------------------Interaccion entre Funciones: ------------------

#Lista inicial
palitos = ['-', '--', '---', '----']

#Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)


#Comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento - 1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)



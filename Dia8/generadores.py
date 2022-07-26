# Los GENERADORES son un tipo especial de funcion que en vez de devolvernos un valor terminado, va produciendo
# ese valor poco a poco a medida que lo vayamos necesitando.
# La funcion generadora a diferencia de una funcion normal, va generando los valores a medida que se los solicita,
# por lo que en terminos de rendimiento de memoria, es mucho mas eficiente.
# en lugar de RETURN se utiliza YIELD (Producir)

# Esta funcion ya ha producido el 4 y lo ha devuelto.
def mi_funcion():
    return 4

# Esta preparado para cuando le pidamos el numero lo produzca en el momento.
def mi_generador():
    yield 4

print(mi_funcion())
print(mi_generador()) # no produjo el 4, solo nos indica que hay un objeto generador

g = mi_generador()

print(next(g)) # Ahora si tenemos el 4. Con next() le indicamos que nos devuelva el siguiente numero.
# Dado que no hay un siguiente numero, si le pedimos el proximo nos dara un error (StopIteration)

def funcion_normal():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

# La funcion generadora recordara donde dejo la ejecucion para ir devolviendome el numero adecuado en el momento solicitado
def funcion_generadora():
    for x in range(1,5):
        yield x * 10

print(funcion_normal()) # [10, 20, 30, 40]
print(funcion_generadora())

generador = funcion_generadora()

print(next(funcion_generadora())) # 10
print(next(funcion_generadora())) # 20
print(next(funcion_generadora())) # 30
print(next(funcion_generadora())) # 40

def otro_generador():
    # En el primer next devuelve el primer yield (1)
    x = 1
    yield x
    # En el segundo next devuelve el segundo yield (2)
    x+=1
    yield x
    # En el tercer next devuelve el tercer yield (3)
    x+=1
    yield x

generador2 = mi_generador()

print(next(generador2)) # 1
print(next(generador2)) # 2
print(next(generador2)) # 3
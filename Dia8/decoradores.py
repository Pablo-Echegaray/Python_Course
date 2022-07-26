# Todo en python es un objeto. Los decoradores son funciones y las funciones son objetos.
# No solo existen los decoradores que python ha creado, sino que podemos crear nuestros propios decoradores.
# los DECORADORES son funciones que modifican el comportamiento de otras funciones y ayudan a acortar nuestro codigo.
'''
def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

def una_funcion(funcion):
    return funcion

funcion = mayuscula
funcion("Puedo asignar funciones a variables")
una_funcion(mayuscula("probando"))
'''
'''
def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula
# Se le asigna la funcion a la variable y se le indica el tipo que se quiere
operacion = cambiar_letras('may')
# Se le indica la palabra y en base al tipo indicado anteriormente va a utilizar una u otra funcion interna de cabiar_letras
operacion('palabra') # PALABRA
'''

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion
'''
@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())
'''

def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())

# Para evitar el uso de @decorador y poder ejecutar la funcion con y sin el planteamos lo siguiente :
mayuscula_decorada = decorar_saludo(mayusculas)

mayuscula_decorada('python') #activamos le decorador.
mayusculas("Python") # Ejecucion sin decorador.
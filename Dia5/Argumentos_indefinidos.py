# Con "*args" le indicamos a la funcion que los parametros que recibira seran indefinidos.
# por convencion se utiliza como palabra "args" pero podria ser cualquier palabra.

def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

def suma2(*args):
    return sum(args)

print(suma(1,2,3,4,5))
print(suma2(4,100,11))

# **kwargs : podemos recibir mas de un argumento al igual que *args, pero con la diferencia que podemos darle un nombre
# a los argumentos. Pudiendo acceder a ellos a traves de un diccionario, y de esta manera obtener el item completo,
# o solamente su clave, o solamente su valor.

def sumar(**kwargs):
    print(type(kwargs))

sumar(x=3, y=5, z=2)

#-----------------------------------------------------

def adicion(**kwargs):
    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(adicion(x=3, y=5, z=2))

#----- FUNCION CON MAS DE UN TIPO DE ARGUMENTO ---------------------------

def prueba(num1, num2, *args, **kwargs):


    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {args}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

#prueba(15,50,100,200,300,x='uno',y='dos',z='tres')
args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(15,50, *args, **kwargs)
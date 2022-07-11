#from random import randint
from random import *

# randint() nos devuelve un entero aleatorio dentro del rango que le inquemos :
aleatorio = randint(1,50)

print(aleatorio)

# uniform() nos devuelte un decimal aleatorio dentro del rango que le indiquemos :
#round(numero a redondear, cantidad de decimales post coma)
aleatorio_uniform = round(uniform(1,5), 1)
print(aleatorio_uniform)

# random() nos devuelve un numero aleatorio decimal entre 0 y 1. No toma argumentos de entrada.
aleatorio_random = random()
print(aleatorio_random)

# choice() nos devuelve un elemento aleatorio de la lista que le pasemos como parametro.
colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio_choise = choice(colores)
print(aleatorio)

# shuffle() ordena de forma aleatoria una lista que le indiquemos como parametro.
numeros = list(range(5,50,5))#Una lista del 5 al 50 de 5 en 5.
#shuffle() no puede ser utilizado con Strings ya que estos son inmutables, tampoco hace un return de un valor.
shuffle(numeros)

print(numeros)
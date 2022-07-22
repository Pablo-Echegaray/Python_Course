# Exclusivamente en Pycharm ->
from os import system

nombre = input("Dime tu nombre : ")
edad = input("Dime tu edad : ")

# Limpiamos la consola para que solo muestre el resultado.
system('cls')
print(f"Tu nombre es {nombre} y tienes {edad} años")
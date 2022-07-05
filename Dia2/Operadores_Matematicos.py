x = 6
y = 2
z = 7

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

#Division al piso -> eliminar todo decimal
print(f"{z} dividido al piso de {y} es igual a {z//y}")
print(f"{z} modulo de {y} es igual {z%y}")
print(f"{x} elevado a la {y} es igual {x**y}")
print(f"{x} elevado a la {3} es igual {x**3}")
print(f"La raiz cuadrada de {x} es {x**0.5}")

#Redondeo
valor = 95.7777777
# valor a redondear, cantidad de decimales
print(round(valor,2))
print(round(valor))
num1 = round(13/2,0)
print(num1)#6.0 (float)
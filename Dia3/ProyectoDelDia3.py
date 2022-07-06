# Pedir al usuario que ingrese un texto.
# Luego pedir tambien que ingrese 3 letras.

# El programa debera :
# ----> Indicar cuantas veces aparece cada letra
# ----> Cuantas palabras hay en total en el texto
# ----> Cual es la primera letra del texto y la ultima
# ----> Mostrar las palabras en orden inverso
# ----> Aparece la palabra 'python' en el texto ?

INPUT = input("Ingrese un texto : ").lower()
LETRA_1= input("Ingrese una letra : ").lower()
LETRA_2= input("Ingrese una segunda letra : ").lower()
LETRA_3= input("Ingrese una tercer letra : ").lower()

lista = [LETRA_1, LETRA_2, LETRA_3]

print(INPUT)
print(lista)

counter_letra_primera = INPUT.count(lista[0])
counter_letra_segunda = INPUT.count(lista[1])
counter_letra_tercera = INPUT.count(lista[2])

lista_input = INPUT.split(" ")
cantidad_palabras = len(lista_input)
print("La transformacion del texto en lista es : " + str(lista_input))
print("La cantidad de palabras del texto es : " + str(cantidad_palabras))
print("El texto a la inversa se ve asi : " + INPUT[: : -1])
print("La primer letra del texto es : " + INPUT[0])
print("La ultima letra del texto es : " + INPUT[-1])
print("python" in INPUT)

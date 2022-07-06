texto = "Este es el texto de Federico"

resultado = texto.split("t")
#crea una lista separando los elementos cada vez que encuentra una 't'

print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

resultado = texto.find("s") # 1 = indice de la primer 's'
#La diferencia con index() es que si no encuentra el caracter que le pasamos devuelve -1

print(resultado)

resultado = texto.replace("Federico", "todos")
# Reemplaza 'Federico' por 'todos'

print(resultado)

resultado = texto.replace("e", "x")
# Reemplaza todas las 'e' por la 'x'

print(resultado)

#Propiedades
#Los strings son inmutables, no asi el valor de la variable que los almacenan
cadena = "Pablo"
cadena[0] = "L" #Esto nos da error
cadena = "Kevin" #Esto si es valido

#String de mas de una linea
poema = """Los peces son blancos
como si el agua
hirviera de calor"""

print(poema) #con el uso de las tres comillas se respeta el salto de linea.

#Pueden multiplicarse
print(cadena * 3) #PabloPabloPablo

#Verificar si una determinada palabra se encuentra en el string
print("Los" in poema) #True
print("peces" not in poema) #False
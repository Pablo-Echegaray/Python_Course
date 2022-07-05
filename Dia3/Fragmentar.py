# SLICING

texto = "ABCDEFGHIJKLM"

fragmento = texto[2 : 5]
#CDE (el caracter 2 se incluye y el 5 no)
# texto[2:] -> Si omitimos el segundo factor nos trae hasta el final
# texto[:5] -> Si omitimos el primer factor, nos trae desde el indice 0 hasta el indice 5 (no incluido)
# texto[2:10:2] -> Toma desde el caracter con indice 2 hasta el 10 (sin incluirlo) saltando de a uno (este si, este no)
# --------> CEGI
# texto[::3] -> Toma todos los caracteres saltando de 3 en 3
# --------> ADGJM
# texto[::-2] -> Toma la cadena a la inversa y va salteando de a uno


print(fragmento)
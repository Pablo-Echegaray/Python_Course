monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:print("No tengo mas dinero")

#------------------------------------------------------------
respuesta = 's'

while respuesta == 's':
    respuesta = input("quieres seguir ? (s/n)")
else:
    print("Gracias")

#-----------------------------------------------------------

#while respuesta = 's'
    #pass ->Se utiliza pass para reservar un espacio en el while cuando aun no sabemos que accion se llevara a cabo,
        # De esta manera nos permite seguir codeando sin obligarnos a completar el while.

#--------------------------------------------------------------------

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        break #Cancela la ejecucion del programa si una letra del nombre es la 'r'. Federico -> Fede
        #continue -> interrumpe el for pero vuelve a ejecutarlo desde donde habia quedado. Federico -> Fedeico
    print(letra)

#-----------------------------------------------------------------

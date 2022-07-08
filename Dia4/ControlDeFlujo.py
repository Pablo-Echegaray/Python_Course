mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tiens un pez')
else:
    print('Nose que animal tienes')

#---------------------------------------------------------------------------

edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')

#-----------------------------------------------------------------------
habla_ingles = True
sabe_python = False

if sabe_python and habla_ingles:
    print("Cumples con los requisitos para postularte")
elif sabe_python and not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif not sabe_python and habla_ingles:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")










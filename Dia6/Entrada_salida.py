mi_archivo = open('prueba.txt')
print(mi_archivo)

#print(mi_archivo.read())

una_linea = mi_archivo.readline()
print(una_linea) # primera linea !

#El sistema guarda un punto de donde habia leido y en la proxima ejecucion del readline() continua leyendo a partir de ese punto.
#Por lo tanto leera la linea siguiente.
una_linea = mi_archivo.readline()
print(una_linea.rstrip()) # segunda linea !! -> rstrip() elimina los saltos de linea

una_linea = mi_archivo.readline()
print(una_linea.upper()) # tercera linea !!!

mi_archivo.close()
# El valor guardado en la variable "una_linea" no deja de ser un string, por lo tanto podemos aplicar todos los metodos
# correspondientes a los strings.
print("\n"+ "*" *30 + "\n")

segundo_archivo = open('prueba2.txt')
'''
for l in segundo_archivo:
    print("Aqui dice: " + l)
'''
# Leer todas las lineas devuelve una lista con c/ linea como elemento. Cuidado al utilizar este metodo, ya que al manipular
# archivos muy extensos utilizando este metodo se puede sobrecargar la memoria.
todas = segundo_archivo.readlines() # lista de nuestras lineas

ultima_linea = todas.pop() #eliminamos la ultima linea
print(ultima_linea)
print(todas)
segundo_archivo.close()

# Toda la manipulacion realizada en este archivo no modifica los datos originales en los archivos, sino que
# solo manipulamos aquello que vamos a mostrar.

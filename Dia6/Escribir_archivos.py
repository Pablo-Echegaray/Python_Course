archivo = open('prueba1.txt', 'w')
# Por defecto el segundo parametro es 'r', que significa que solo
# vamos a realizar acciones de lectura sobre el archivo.
# 'w' : escribir (si posee texto, este sera reemplazado. Si el texto no existe, lo creara)
# 'w' -> no genera saltos de linea automaticos.
# 'a' : escribir a partir del ultimo punto del archivo (conserva el texto original)
# El parametro 'a' es muy utilizado por devs cuando quieren escribir un log de registro
# de actividad de un programa, para que cada vez que se haga algo en un programa,
# quede registrado en un archivo. Esto permite que se vayan agragando los registros
# cada vez que se utiliza el programa al final.
archivo.write('''Hola Mundo
estamos escribiendo
archivos''')

# writelines() -> toma una lista de Strings y concatena cada elemento uno al lado del otro
# en una unica linea.


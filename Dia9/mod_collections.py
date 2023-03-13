from collections import Counter
from collections import defaultdict
from collections import namedtuple

numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]
# Counter() nos indica cuantas veces se repite un elemento de nuestra lista. Nos devuelve un "diccionario" con esa info.
print(Counter(numeros))
print(Counter('mississipi'))

frase = 'al pan pan y al vino vino, sobre las cartas la mesa'
print(Counter(frase.split()))

serie = Counter([1,1,1,1,2,2,2,2,3,3,3,3,4])
# most_common() -> mas comun -> Nos ordena nuestra lista en tuplas, en funcion de la cantidad de apariciones
# de mayor a menor [(elemento1, cantidad), (elemento2,cantidad)]
# most_common(1) nos mostrara solo el elemento que mas se repite,
# most_common(2) nos mostrara los dos elementos que mas se repiten, y asi
print(serie.most_common())

#################################################################################

# defaultdict

mi_dic = {'uno':'verde', 'dos':'azul','tres':'rojo'}

print(mi_dic['cuatro']) # Esto nos tirara error ya que la clave no existe
# Esto podria ser un problema si iteramos sobre una lista de claves donde haya una que no exista.


mi_dict = defaultdict(lambda: 'nada')
mi_dict['uno'] = 'verde'
print(mi_dic['dos']) # nada

print(mi_dic)

######################################################################################

Persona = namedtuple('Perosona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

print(ariel.altura) #1.76
print(ariel.peso) #79
print(ariel[2]) #79


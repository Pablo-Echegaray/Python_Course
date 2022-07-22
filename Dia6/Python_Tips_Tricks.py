# Dictionaries ->

var_dict:dict = {
  'field1':'value1'
}

# esta línea arroja error porque el campo no existe
#print(var_dict['field2'])

# el get es la forma segura de leer el att, si no existe devuelve None
print(var_dict.get('field2'))

# se le puede setear un valor default en caso de que no exista o sea None
print(var_dict.get('field2', 'default_value'))

# crear un nuevo atributo dentro de un dict
var_dict['field2'] = 'value2'
print(var_dict['field2'])

# *************************************************************************************************
# Conversion de Datos ->

# str => int
var_int:int = int("1")

# dict => json
import json
dictionary ={
  "field1": "value1",
  "field2": "value2"
}
json_object = json.dumps(dictionary, indent = 4)
print(json_object)
print(f"Sin castearlo a json : {dictionary}")

#**********************************************************************************************************
# Concatenacion de Datos ->
# strings
var_str = 'texto1' + ' ' + 'texto2'
# result => 'texto1 texto2'

# dictionaries
var_dict = {'field1':'value1'} | {'field2':'value2'}
# result => {'field1':'value1', 'field2':'value2'}

# lists
var_list = [1,2,3] + [4,5,6]
# result => [1,2,3, 4,5,6]

#******************************************************************************************************
# Manejo de Strings ->
# extraer 2 primeros caracteres
var_str:str = "hola"
first_two = var_str[:2]

# extraer 3 últimos caracteres
var_str:str = "chau"
last_three = var_str[-3:]

# dividir string por un caracter
var_str:str = "a,b,c,d"
var_list:list = var_str.split(",")

# dividir string por new line
'''línea1
línea2
línea3
'''
var_list:list = var_str.splitlines()

#**************************************************************************************************************
# If Clauses / Elvis operator (Ternary conditional operator) ->
# not / in / and / or / == / !=
var_str: str = "a"
if var_str not in ['b', 'c']:
  print("No está dentro de la lista [b, c]")
elif var_str == 'a' or var_str == 'b':
  print("Es a o b")

# chequear lista vacia
var_list: list = []
if not var_list: print("Lista vacía")

# Elvis operator (Ternary conditional operator)
# lo que antes era variable?:"default_value_si_variable_es_null"
a = "a"
b = "b"
var = (a if a != None else b)

# *******************************************************************************************************
# Constructor + Self ->
class Person():
  def __init__(self, name: str, last_name: str):
    self.name = name
    self.last_name = last_name

  def get_name(self) -> str:  # nótese el primer (y único en este caso) parámetro
    return self.name

  def get_last_name(self) -> str:
    return self.last_name

  def get_full_name(self) -> str:
    return f"{self.get_name()} {self.get_last_name()}"  # nótese el uso de self para llamar a las otras funciones

# Main ->
if __name__ == '__main__':
  person = Person("Kevin", "McCallister")
  print(f"El nombre de la persona es: {person.get_full_name()}")

# List => Loop (condicionado) /  Filter / Find / Map / Any / Size / Sum ->
items:list[dict] = [
  {'quantity':1, 'warehouse_id':'BRSP02'},
  {'quantity':2, 'warehouse_id':'ARBA01'}
]

# loop
for item in items:
  print(f"{item['warehouse_id']}: {item['quantity']}")

# filter
item_matches:list = list(filter(lambda item: item['quantity']>0, items))

#for condicionado por un filter
for item in filter(lambda i: i['warehouse_id']=='BRSP02', items): print("Algo")

# find_all (filtrar y obtener parte de los atributos, en este caso warehouse_id)
warehouse_matches = list(i['warehouse_id'] for i in items if i['quantity']==1)

# find_first
item = next((item for item in items if item['warehouse_id']=='BRSP02'), None)

# map (obtener parte de los atributos, en este caso warehouse_id)
warehouses = list(map(lambda item: item['warehouse_id'], items))

#any
any(item['warehouse_id']=='BRSP02' for item in items)

#sum
sum(item['quantity'] for item in items)
#sum + if
sum(item['quantity'] for item in items if item['warehouse_id']=='BRSP02')

# size
len(items)

# List => GroupBy + Multiple columns ->
from itertools import groupby, starmap
import json

batches = [
    {"batch_id": 1, "group_id": 1001, "inventory_id": "AAA111", "unit_id": "AAA111-1", "unit_status": "active"},
    {"batch_id": 2, "group_id": 1002, "inventory_id": "AAA222", "unit_id": "AAA222-1", "unit_status": "active"},
    {"batch_id": 3, "group_id": 1003, "inventory_id": "AAA333", "unit_id": "AAA333-3", "unit_status": "active"},
    {"batch_id": 1, "group_id": 1001, "inventory_id": "AAA111", "unit_id": "AAA111-2", "unit_status": "active"},
    {"batch_id": 3, "group_id": 1003, "inventory_id": "AAA333", "unit_id": "AAA333-2", "unit_status": "active"},
    {"batch_id": 2, "group_id": 1002, "inventory_id": "AAA222", "unit_id": "AAA222-2", "unit_status": "active"},
    {"batch_id": 1, "group_id": 1001, "inventory_id": "AAA111", "unit_id": "AAA111-3", "unit_status": "active"},
    {"batch_id": 2, "group_id": 1002, "inventory_id": "AAA222", "unit_id": "AAA222-3", "unit_status": "active"},
    {"batch_id": 3, "group_id": 1003, "inventory_id": "AAA333", "unit_id": "AAA333-1", "unit_status": "active"}
]

# NOTAS:
# - groupby no funciona con map, motivo por el cual hay que usar starmap
# - groupby requiere que la lista esté ordenada previo a agrupar
# - en cada inventory debería agregarle "quantity": len(units) pero units es un iterator
#   y el len hace que se itere y luego deja vacío el atributo "units"

by_batch     = lambda x:x['batch_id']
by_group     = lambda x:x['group_id']
by_inventory = lambda x:x['inventory_id']

batches_json = list(starmap(lambda batch_id, groups: {
                    "batch_id": batch_id,
                    "groups": list(starmap(lambda group_id, inventories: {
                        "group_id": group_id,
                        "inventories": list(starmap(lambda inventory_id, units: {
                            "inventory_id": inventory_id,
                            "units": list(map(lambda u: {
                                "unit_id": u['unit_id'],
                                "unit_status": u['unit_status']
                            }, units))
                        }, groupby(sorted(inventories, key=by_inventory), key=by_inventory)))
                    }, groupby(sorted(groups, key=by_group), key=by_group)))
                }, groupby(sorted(batches, key=by_batch), key=by_batch)))


for batch in batches_json:
    for group in batch['groups']:
        for inventory in group['inventories']:
            inventory['quantity'] = len(inventory['units'])

print(json.dumps(batches_json, indent=4))

### Output
'''
[
    {
        "batch_id": 1,
        "groups": [
            {
                "group_id": 1001,
                "inventories": [
                    {
                        "inventory_id": "AAA111",
                        "units": [
                            {
                                "unit_id": "AAA111-1",
                                "unit_status": "active"
                            },
                            {
                                "unit_id": "AAA111-2",
                                "unit_status": "active"
                            },
                            {
                                "unit_id": "AAA111-3",
                                "unit_status": "active"
                            }
                        ],
                        "quantity": 3
                    }
                ]
            }
        ]
    },
    etc...
] '''

# Sample - Multi Columns
from itertools import groupby, starmap
import json

batches = [
    {"order_id": 1, "warehouse_id": 1001, "inventory_id": "AAA111"},
    {"order_id": 2, "warehouse_id": 1002, "inventory_id": "AAA222"},
    {"order_id": 3, "warehouse_id": 1003, "inventory_id": "AAA333"},
    {"order_id": 1, "warehouse_id": 1001, "inventory_id": "AAA222"},
    {"order_id": 3, "warehouse_id": 1003, "inventory_id": "AAA333"},
    {"order_id": 2, "warehouse_id": 1002, "inventory_id": "AAA222"},
    {"order_id": 1, "warehouse_id": 1001, "inventory_id": "AAA111"},
    {"order_id": 2, "warehouse_id": 1002, "inventory_id": "AAA222"},
    {"order_id": 3, "warehouse_id": 1003, "inventory_id": "AAA333"}
]

by_keys = lambda x:(x['order_id'], x['warehouse_id'])

batches_json = list(starmap(lambda keys, inventories: {
                    "order_id": keys[0],
                    "warehouse_id": keys[1],
                    "inventories": list(inventories)
                }, groupby(sorted(batches, key=by_keys), key=by_keys)))

print(json.dumps(batches_json, indent=4))

# Sort by Date (parse date) ->
#from dateutil import parser

data_list = [
    {"field": "a", "date_as_string": "2021-09-04T12:43:01.845993-04:00"},
    {"field": "b", "date_as_string": "2021-09-05T12:43:01.845993-04:00"}
]

#print(sorted(data_list, reverse = True, key=lambda data: parser.parse(data['date_as_string'])))

# RateLimiter ->
from ratelimit import limits, sleep_and_retry
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import time, datetime

PERIOD_IN_SECONDS = 10
MAX_CALLS_PER_PERIOD = 20

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_PERIOD, period=PERIOD_IN_SECONDS)
def access_rate_limited_api(count):
    print(f"{count} - {datetime.datetime.now()}")
    time.sleep(1)

if __name__ == '__main__':
    with PoolExecutor(max_workers=10) as executor:
        executor.map(access_rate_limited_api, list(range(60)))

# att.get(“key”,  “default_value”) ->
# idem a lo que vimos con dict pero con variables de entorno
# client_id:str = os.environ.get('CLIENT_ID', '2593007342846812')

# Exceptions/Errors => Raise / Try / Catch
'''
try:
  raise ValueError("Esto es un ValueError")
except ValueError, KeyError as e:
  print(str(e))  #sólo el texto
  print(repr(e)) #más detalle (feo para el usuario, útil para nosotros)
except Exception as e:
  print(str(e))
'''
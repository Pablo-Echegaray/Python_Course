#
mi_lista = [1,1,1,1,1,1,1]

print(len(mi_lista))

class Objeto:
    pass

mi_objeto = Objeto()

# print(len(mi_objeto)) # Error

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    # metodo toString()
    def __str__(self):
        # Este metodo especial nos ayuda a definir la forma en que yo quiero que se manifieste,
        # un string de mi clase cada vez que algun metodo lo solicite.
        return f"Album : {self.titulo} de {self.autor}"
    # Se define el len() para mi objeto y se le indica que en este caso el concepto de largo
    # hara referencia a la cantidad de canciones del cd.
    def __len__(self):
        return self.canciones
    # Le decimos a del que ademas de eliminar una instancia, haga un print luego de eliminarla,
    # Tambien podriamos configurar a del para que no borre nuestra instancia.
    def __del__(self):
        print("Se ha eliminado el cd")

mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)
print(len(mi_cd))

# Todos los objetos tienen en su metodo __str__ su representacion en formato string.

del mi_cd # esta funcion elimina la instancia del objeto que le indiquemos
# En principio del al eliminar una instancia no informa que la misma haya sido eliminada,
# pero ello podemos definirlo en la clase del objeto instanciado previamente y borrado despues.

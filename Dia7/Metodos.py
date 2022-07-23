# Decoradores : nos permiten crear diferentes tipos de metodos.

# Metodos de instancia : sin decorador.
'''  def mi_metodo(self):
         print("algo")
Son metodos que una vez que han sido creados pueden ser llamados. Pueden acceder y modificar los
atributos del objeto,
Pueden acceder a otros metodos,
Dado que desde cada objeto tambien se puede acceder a la clase, tambien pueden modificar el estado de
la clase.
Los metodos de instancia afectan a cada instancia (al self).
'''
# Metodos de clase : @classmethod
''' @classmethod
    def mi_metodo(cls):
        print("algo")
En lugar de "self" ponemos "cls" por clase. Estos metodos no estan asociados a las instancias de las 
clases, sino a la clase en si misma,
Por lo tanto pueden ser llamados no solamente desde una instancia de nuestra clase,sino tambien 
directamente desde una clase.
Estos metodos a diferencia de los metodos de instancia, no pueden acceder a los atributos de instancia,
pero si pueden modificar por supuesto los atributos de la clase.        
'''
# Metodos estaticos : @staticmethod
''' @staticmethod
    def mi_metodo():
        print("algo")
No aceptan como parametro ni "self" ni "cls".
No pueden modificar el estado ni de la clase ni de la instancia, pero por supuesto pueden aceptar
parametros de entrada.
Por lo tanto el uso de los metodos estaticos puede resultar util para indicar que un metodo no podra
modificar el estado de la instancia ni de la clase.
En otras palabras los metodos estaticos se podrian ver como funciones normales, de esas que usamos
fuera de una clase, con la salvedad de que estos si van ligados a una clase concreta.       
'''

class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")
        #Al ser un metodo de instancia puede acceder a otros metodos.
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
       # print(f"Es de color {self.color}") Da error por ser un atributo de instancia
        cls.alas = False
        #Podemos solo modificar y acceder a atributos de clase
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.mirar()
Pajaro.poner_huevos(3) # Al ser un metodo de clase podemos acceder a el sin instanciar la clase.


piolin = Pajaro("amarillo", "canario")
piolin.alas = False

print(piolin.alas)
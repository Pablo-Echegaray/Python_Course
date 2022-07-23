class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        #self.edad = edad
        #self.color = color
        super().__init__(edad,color)

        self.altura_vuelo = altura_vuelo

    # Sobreescritura de metodos
    def hablar(self):
        print("pio")

piolin = Pajaro(3, "amarillo", 60)

#################### HERENCIA MULTIPLE ##############################################

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print('ja ja')

    def hablar(self):
        print("que tal")

#Hijo Hereda de Padre y Madre
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.reir()
# Nieto al hablar dira "HOLA" Ya que primero heredo de Padre y no de Madre.
mi_nieto.hablar()

# mro = method resolution orden (orden de reolucion de los metodos) En este caso el orden de resolucion
# es el siguiente :
# 1- Nieto, 2- Hijo, 3- Padre, 4- Madre, 5- Object
print(Nieto.__mro__)

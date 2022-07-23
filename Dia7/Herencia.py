### 6 Principios basicos de POO :
# 1- Herencia
# 2- Polimorfismo
# 3- Cohesion
# 4- Abstraccion
# 5- Acoplamiento
# 6- Encapsulamiento

#### Herencia ####
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

# Este atributo nos dice de quien hereda Pajaro
print(Pajaro.__bases__)

# Indica las clases que heredan de Animal
print(Animal.__subclases__())

piolini = Pajaro(2,"amarillo")
print(piolini.color)
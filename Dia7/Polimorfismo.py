class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice meee")

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

vaca1.hablar()
oveja1.hablar()


def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)
animal_habla(vaca1)
# Sin importar que se trate de dos objetos distintos, la funcion animal_habla() puede ejecutar
# el metodo hablar() de ambos, por mas que se trate de dos objetos distintos con dos implementaciones
# diferentes de su metodo hablar(). Esto es polimorfismo.
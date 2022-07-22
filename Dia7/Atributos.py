class Pajaro:
    # Constructor self = this
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro', 'Tucan')

print(mi_pajaro.color)
print(mi_pajaro.especie)
# <Same>
print(Pajaro.alas)
print(mi_pajaro.alas)
# </Same>
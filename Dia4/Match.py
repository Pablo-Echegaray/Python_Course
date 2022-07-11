serie = "N-02"

'''if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")'''

# Hasta antes de python 3.10 al no exisitir en el lenguaje el switch case, tratabamos las multiples opciones con
# un if y varios elif.
# Con la llegada de Match, nos va a permitir hacer esto de una manera distinta.

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

# ---------- Potencia de match -----------
cliente = {'nombre': 'Pablo', 'edad': 45, 'ocupacion': 'instructor'}
pelicula = {'titulo': 'Matrix', 'ficha_tecnica': {'protagonista': 'Keanu reeves','director':'Lana y Lilli wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")
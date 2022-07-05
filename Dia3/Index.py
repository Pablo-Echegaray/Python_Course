#index() -> nos devuelve la posicion o la letra que se encuentra en el indice que le indiquemos
mi_texto = "Esta es una prueba"
resultado = mi_texto[-1] #a
resultado2 = mi_texto[5] #e

resultado3 = mi_texto.index("n")#9
resultado4 = mi_texto.index("prueba")#12 -> nos dice el indice donde comienza la palabra
resultado5 = mi_texto.index("a")#3 nos devuelve el indice de la primer 'a' que encuentra
resultado6 = mi_texto.index("a",5)#Empieza a contar desde el indice 5
#resultado7 = mi_texto.index("a",5,10)#Empieza a contar desde el indice 5 hasta el 10

# rindex() -> busca en reversa
#resultado8 = mi_texto.rindex("a")#17
print(resultado)
print(resultado2)
print(resultado3)
print(str(resultado4)+"\n\t\tHola")
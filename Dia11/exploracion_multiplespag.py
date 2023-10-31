import bs4
import requests


url_base = "http://books.toscrape.com/catalogue/page-{}.html"

'''
for n in range(1,11):
    print(url_base.format(n))
'''
# El article posee la clase product_pod, y este es el que contiene la tarjeta del libro con su valoracion en estrellas, donde estas se encuentra en un p con la clase start-rating donde la cantidad de estrellas que posee se determinan a partir de una segunda clase que basicamente indica la cant de estrellas en ingles. Por ej: <p class= star-rating Three>

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa.select('.product_pod'))

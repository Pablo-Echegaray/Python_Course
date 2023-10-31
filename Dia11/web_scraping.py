import bs4
import requests

# Web a scrapear
resultado = requests.get('https://escueladirecta-blog.blogspot.com/')
#print(resultado.text)

# Parse del codigo html recibido como string
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# Traemos una etiqueta en particular.
#print(sopa.select('title'))

# Traemos solo el texto de la etiqueta.
#print(sopa.select('title')[0].getText())

parrafo_especial = sopa.select('li')[0].getText()
#print(parrafo_especial)

# select() seria como el querySelector() de JS

##############################################################
response = requests.get('https://www.escueladirecta.com/courses')
sopa2 = bs4.BeautifulSoup(response.text, 'lxml')

imagenes = sopa2.select('.course-box-image')[0]['src']

#print(imagenes)

imagen_curso1 = requests.get(imagenes)
#print(imagen_curso1)
print(imagen_curso1.content)

# wb : write binario
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso1.content)
f.close()


# -*- coding: latin-1 -*-
import requests

def clonar(url):
    datos= requests.get(url)
    guarda=open("Cuarentena.html", "wb")
    guarda.write(datos.content)
    return "Página clonada..."
datos=clonar("https://cuarentenaa.es/")
print(datos)

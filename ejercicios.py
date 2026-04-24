import csv
import statistics
import requests 

URL = "http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=5000"

def recoleccionDeDatos():
    r = requests.get(URL)         
    # la respuesta viene en dos partes; el segundo elemento es la lista de datos
    paises = [pais["country"]["value"] for pais in r.json()[1]] #RECOLECTAMOS TODOS LOS DATOS
    return paises

def limpiador_datos(paises=None):
    return list(dict.fromkeys(paises))

# Ejecutar y mostrar resultados
paises = recoleccionDeDatos()
paises_unicos = limpiador_datos(paises)
print(paises_unicos)

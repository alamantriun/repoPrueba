import csv #no hemos creado el reporte
import statistics #para hacer procesos estadisticos
import requests #para pedir informacion de la api

URL = "http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=5000" #pedimos informacion de la api que esta en una URL
                                                                                                #esto es como un puente pero falta la entrada

def obtener_datos():#funcion para pedir los datos // Esta es la entrada

    r = requests.get(URL)#la puerta 

    return ([pais["country"] for pais in r.json()[1][23:30]]) #recorre los datos del data set [1] = 2 (este contiene la informacion principal si miramos el JSON)
    
    #ESTO LO TENEMOS QUE DOMINAR
    
def limpiar_datos(datos):
    limpios = []
#esto tambien lo tenemos que dominar
    for d in datos:
        if d["value"] is not None:
            limpios.append({
                "pais": d["country"]["value"],
                "año": d["date"],
                "valor": d["value"]
            })
#hasta aca
    return limpios

def calcular_estadisticas():
    valores = [d["valor"] for d in datos]

    promedio = statistics.mean(valores) if valores else 0
    maximo = max(valores) if valores else 0
    minimo = min(valores) if valores else 0

    return promedio, maximo, minimo



datos = obtener_datos()
datos_limpios = limpiar_datos(datos)






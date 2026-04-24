# Importar librerías necesarias para hacer peticiones HTTP, trabajar con CSV y cálculos estadísticos
import requests
import csv
import statistics

# URL de la API del Banco Mundial para obtener población total de Colombia, Argentina y Brasil
URL = "https://api.worldbank.org/v2/country/col;arg;bra/indicator/SP.POP.TOTL?format=json"

# Función que obtiene los datos de la API
def obtener_datos():
    r = requests.get(URL)  # Hacer petición GET a la API
    return r.json()[1]  # Retornar el índice 1 del JSON (datos principales)

# Función que filtra y organiza los datos válidos
def limpiar_datos(datos):
    limpios = []
    for d in datos:
        # Solo procesar registros que tengan valor
        if d["value"] is not None:
            limpios.append({
                "pais": d["country"]["value"],  # Nombre del país
                "anio": d["date"],  # Año del registro
                "valor": d["value"]  # Valor de la población
            })
    return limpios

# Función que calcula estadísticas de los datos
def calcular_estadisticas(datos):
    valores = []
    # Extraer todos los valores de población en una lista
    for d in datos:
        valores.append(d["valor"])

    # Calcular promedio, máximo y mínimo
    promedio = statistics.mean(valores)
    maximo = max(valores)
    minimo = min(valores)

    return promedio, maximo, minimo

# Función que guarda los datos limpios en un archivo CSV
def guardar_csv(datos):
    with open("estadisticas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["pais", "anio", "valor"])  # Encabezados

        # Escribir cada fila de datos
        for d in datos:
            writer.writerow([d["pais"], d["anio"], d["valor"]])

# Función principal que ejecuta todo el flujo
def main():
    datos = obtener_datos()  # Obtener datos de la API
    datos = limpiar_datos(datos)  # Limpiar y filtrar datos

    promedio, maximo, minimo = calcular_estadisticas(datos)  # Calcular estadísticas

    guardar_csv(datos)  # Guardar en CSV

    # Mostrar resultados
    print("📊 REPORTE")
    print("Promedio:", promedio)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)

# Ejecutar programa
main()

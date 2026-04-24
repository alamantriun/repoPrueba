

curso_actual = float(1.5)
el_mas_lento = float(7.0)
el_mas_rapido = float(2.5)
promedio = float(4.0)

diferencia_con_el_mas_lento = (curso_actual / el_mas_lento) * 100
print(f"Diferencia con el más lento: {diferencia_con_el_mas_lento:.1f}%")
diferencia_con_el_mas_rapido = (curso_actual / el_mas_rapido) * 100
print(f"Diferencia con el más rápido: {diferencia_con_el_mas_rapido:.1f}%")
diferencia_con_el_promedio = (curso_actual / promedio) * 100
print(f"Diferencia con el promedio: {diferencia_con_el_promedio:.1f}%")


texto = input("Ingrese un texto: ").split(" ")
print(f"El texto tiene {len(texto)} palabras.")
print(f"La duracion del texto es: {len(texto)/2} segundos.")
print(f"dalto lo diria en {len(texto)/2*1.3} segundos de duracion.")

if len(texto)/2 > 60:
    print("es demasiado largo mija")

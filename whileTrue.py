import random as rd

numOculto = rd.randint(1, 10)
n_intentos = 3

while n_intentos > 0:
    try:
        adivina = int(input("Adivina el número (entre 1 y 10): "))
        if adivina == numOculto:
            print(f"¡Felicidades, ganaste! El número era {numOculto}")
            break
        else:
            n_intentos -= 1
            if n_intentos > 0:
                print(f"Incorrecto. Intenta nuevamente, te quedan {n_intentos} intentos")
            else:
                print(f"Perdiste. El número era {numOculto}")
    except ValueError:
        print("Por favor, ingresa un número válido")

print("Gracias por jugar")
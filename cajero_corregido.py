saldo = 100000

def retirar(saldo, numero):
    saldo -= numero
    return saldo

def consultar(saldo):
    print(f"Su saldo es: {saldo}")
    return saldo

def consignar(saldo, numero):
    saldo += numero
    return saldo

while True:
    print("BIENVENIDO AL CAJERO")
    print("1. Para retirar")
    print("2. Para consultar")
    print("3. Para consignar")
    print("4. Para salir del cajero")
    
    try:
        option = int(input("¿Qué desea hacer? "))
        
        if option == 1:
            try:
                cantidad = int(input("¿Cuánto desea retirar? "))
                if cantidad <= 0:
                    print("La cantidad a retirar debe ser mayor a cero.")
                elif cantidad > saldo:
                    print("No tiene suficiente saldo.")
                else:
                    saldo = retirar(saldo, cantidad)
                    print(f"Retiro exitoso. Su nuevo saldo es {saldo}.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un valor numérico.")

        elif option == 2:
            consultar(saldo)
        
        elif option == 3:
            try:
                cantidad = int(input("¿Cuánto desea consignar? "))
                if cantidad <= 0:
                    print("La cantidad a consignar debe ser mayor a cero.")
                else:
                    saldo = consignar(saldo, cantidad)
                    print("Operación exitosa")
                    print(f"Su nuevo saldo es {saldo}.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un valor numérico.")

        elif option == 4:
            print("Chao pescao")
            break
        else:
            print("Opción no válida. Por favor, elija 1, 2, 3 o 4.")
    
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número del 1 al 4.")

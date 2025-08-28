control = True

while control == True:
    N1 = float(input("ingrese un numero "))
    N2 = float(input("ingrese numero "))
    print("S. sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nP. Potencia\nE. Salir")
    opcion = input("elija una opcion: ")
    opcion = opcion.upper()   

    match opcion:
        case "S":
            print("suma")
            resultado = N1 + N2
        case "R":
            print("restar")
            resultado = N1 - N2
        case "M":
            print("multiplicar")
            resultado = N1 * N2
        case "D":
            print("dividir")
            if N2 == 0:
                resultado = ("division no valida")
            else: 
                resultado = N1 / N2
        case "P":
            print("potencia")
            resultado = N1 ** N2    
        case "E":
            control = False
        case _:
            print("modo no valido")
    print(f"resultado = {resultado}")
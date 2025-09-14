'''
variables de entrada
nombre| tipo|
opcion|str|
temperatura|float|

variables de salida
nombre|tipo|
conversion|float|

variable de control
nombre|tipo| 
opcion|str|
'''
opcion = 'A'
while opcion != 'Q':
    print("C. Celsius a Farenheit\nF. Farenheit a Celsius\nQ. salir") 
    opcion = input("elija una opcion: ")
    opcion = opcion.upper()
    if opcion != 'Q':
        temperatura = float(input("ingrese la temperatura: "))
        match opcion:
            case 'F':
                conversion = (temperatura - 32) * (5/9)
                print(f"la temperatura es: {conversion: 0.1f} °C")
            case 'C':
                conversion = (temperatura * 9/5) + 32
                print(f"la temperatura es: {conversion: 0.1f} °F")
            case _:
                print("opcion no valida")
    else:
        print("Saliendo del programa... ;(")           
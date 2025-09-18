from modulos.mod_funciones import *

def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                print("calcula si un numero es primo.")
                valor = int(input("ingresa un entero mayor que 1 >> "))
                primo(valor)
            case 2:
                print("imprime la serie de fibonacci.")
                num = int(input("ingresa el numero de terminos >> "))
                fibonacci(num)
            case 3:
                print("imprime la tabla de multiplicar.")
                num = float(input("ingresa el numero >> "))
                tabla(num)
            case 4:
                break
            case _:
                print("la opcion que ingresó no es valida")

if __name__=="__main__":
    main()

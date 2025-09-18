from modulos.cod_prog import *

def main():
    
    e = True
    while e == True:
        O = menu()
        match O:
            case "C":
                Calcular_Rentabilidad_de_vuelo()
            case "V":
                Verificar_aeronavegabilidad()
            case "R":
                combustible_e1 = int(input("Ingrese la cantidad de combustible de la etapa 1 (kg): "))
                combustible_e2 = int(input("Ingrese la cantidad de combustible de la etapa 2 (kg): "))
                simular_cohete(combustible_e1, combustible_e2)
            case "S":
                print("Saliendo del programa...")
                e = False
            case _:
                print("Opción inválida")

if __name__=="__main__":
    main()

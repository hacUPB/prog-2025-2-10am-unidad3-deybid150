objetivo_alt = 200
consumo_1 = 800
consumo_2 = 500
IA1 = 5
IA2 = 3
 
altitud = 0
minuto = 0
etapa = 1
 
while altitud < objetivo_alt:
    if etapa == 1:
        if combustible_e1 > 0:
                combustible_e1 -= consumo_1
                altitud += IA1
                minuto += 1
        else:
                etapa = 2
    elif etapa == 2:
        if combustible_e2 > 0:
                combustible_e2 -= consumo_2
                altitud += IA2
                minuto += 1
    else:
        print("\nEl cohete se quedó sin combustible en la etapa 2.")
        print("Altitud alcanzada:", altitud, "km")
 
print("\nEl cohete alcanzó la órbita de 200 km en", minuto, "minutos.")
 
while True:
        print("\n--- Simulación de lanzamiento de cohete ---")
        combustible_e1 = int(input("Ingrese la cantidad de combustible de la etapa 1 (kg): "))
        combustible_e2 = int(input("Ingrese la cantidad de combustible de la etapa 2 (kg): "))
    
        simular_cohete(combustible_e1, combustible_e2)
    
        continuar = input("\n¿Desea realizar otra simulación? (SI/NO): ").upper()
        if continuar == "NO":
            print("Simulación finalizada.")
            break
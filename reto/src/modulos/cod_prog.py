def Calcular_Rentabilidad_de_vuelo():
    GH = 12000
    VC = 0.70
    h = 0
    CC = float(input("Ingrese la cantidad total de combustible en kg (40,000 - 254,000): "))
    if 40000 <= CC <= 254000:
        NT = float(input("Ingrese el numero de tickets vendidos (max 853): "))
        if 0 < NT <= 853:
            VT = float(input("Ingrese el valor de cada ticket (400-1500): "))
            if 400 <= VT <= 1500:
                T = float(input("Ingrese la duracion total del vuelo (2-16 horas): "))
                if 2 <= T <= 16:
                    ST = NT * VT
                    VV = CC * VC
                    G = ST - VV
                    while h < T:
                        CC -= GH
                        h += 1
                        if CC <= 0:
                            print(f"El vuelo es inviable, se quedó sin combustible en la hora {h}. Pérdida: {G:0.2f} USD")
                            return
                    if G < 0:
                        print(f"El vuelo no es rentable. Pérdida: {G:0.2f} USD")
                    else:
                        print(f"El vuelo es rentable. Ganancia: {G:0.2f} USD")
                else:
                    print("Duracion del vuelo no permitida")
            else:
                print("Precio no valido")
        else:
            print("Numero de asientos incompatible")
    else:
        print("Cantidad de combustible no valida")


def Verificar_aeronavegabilidad():
    horas_vuelo = int(input("Ingrese las horas de vuelo: "))
    if horas_vuelo >= 600:
        print("Debe realizarse chequeo de mantenimiento al sistema hidráulico.")
    if horas_vuelo >= 400:
        print("Debe realizarse chequeo de mantenimiento al sistema eléctrico.")
    print("Debe realizarse chequeo de mantenimiento al sistema de aire acondicionado.")

    sistema_H = input("Estado del sistema hidráulico (OK/FALLA): ").upper()
    sistema_E = input("Estado del sistema eléctrico (OK/FALLA): ").upper()
    sistema_A = input("Estado del sistema de aire acondicionado (OK/FALLA): ").upper()

    if sistema_H == "FALLA":
        print("Reparación de sistema hidráulico: operación detenida por 2 días.")
        autorizacion = "NO AUTORIZADA"
    elif sistema_E == "FALLA":
        print("Reparación de sistema eléctrico: operación detenida por 3 días.")
        autorizacion = "NO AUTORIZADA"
    elif sistema_A == "FALLA":
        print("Falla en sistema de aire acondicionado: operación restringida a 10.000 pies.")
        autorizacion = "AUTORIZADA CON RESTRICCIÓN"
    else:
        print("Todos los sistemas están bien.")
        autorizacion = "AUTORIZADA"

    print("Estado final de la aeronave:", autorizacion)


def simular_cohete(combustible_e1, combustible_e2):
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
                return

    print("\nEl cohete alcanzó la órbita de 200 km en", minuto, "minutos.")

def menu():
    print("\n--- MENU ---")
    print("C: Calcular rentabilidad de vuelo")
    print("V: Verificar aeronavegabilidad")
    print("R: Simular cohete")
    print("S: Salir")
    return input("Seleccione una opción: ").strip().upper()
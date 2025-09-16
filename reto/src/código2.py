# Registro de mantenimiento de aeronaves A350-900

while True:
    # Ingreso de horas de vuelo
    horas_vuelo = int(input("Ingrese las horas de vuelo: "))

    # Verificación de mantenimientos según horas de vuelo
    if horas_vuelo >= 600:
        print("Debe realizarse chequeo de mantenimiento al sistema hidráulico.")
    if horas_vuelo >= 400:
        print("Debe realizarse chequeo de mantenimiento al sistema eléctrico.")
    print("Debe realizarse chequeo de mantenimiento al sistema de aire acondicionado.")

    # Estado del sistema
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

    # Resultado
    print("Estado final de la aeronave:", autorizacion)

    # Preguntar si desea continuar con otra aeronave
    continuar = input("\n¿Desea registrar otra aeronave? (SI/NO): ").upper()
    if continuar != "SI":
        print("Registro de mantenimiento finalizado.")
        break

# aquí se hizo uso de la IA, para hallar la manera de hacer el bucle hasta que el usuario lo decida.
# Incluyó el While True, if continuar != "SI" y break. Además sugirió el .upper()

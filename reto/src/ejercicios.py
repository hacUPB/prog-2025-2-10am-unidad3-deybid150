e = True

while e == True:
    print("C. Calcular Rentabilidad de vuelo\nV. Verificar aeronavegabilidad\nP. Pago de operadores de rampa\nS. Salir")
    O = input("elija una opcion: ").upper()
    match O:
        case "C":
            GH = 12000
            PA = 276800
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
                                    break
                            else:
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
        case "V":
            while True:
   
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
                continuar = input("\n¿Desea registrar otra aeronave? (SI/NO): ").upper()
                if continuar != "SI":
                    print("Registro de mantenimiento finalizado.")
                    break
        case "P":
            dias_trabajados = 4 * 6  
            umbral_diario = 800
            pago_diario = 60000
            pago_adicional = 50000
            total_maletas = 0
            total_pago = 0
            dias_exceso = 0
            i = 1
            while i <= dias_trabajados:
                # Simulación determinística: días impares = 750, días pares = 850(apoyo con IA Para la simulacion)
                if i % 2 == 0:
                    maletas_dia = 850
                else:
                    maletas_dia = 750

                print(f"Día {i}: {maletas_dia} maletas")

                total_maletas += maletas_dia
                total_pago += pago_diario

                if maletas_dia > umbral_diario:
                    total_pago += pago_adicional
                    dias_exceso += 1
                i += 1
            promedio_diario = total_maletas / dias_trabajados
            print(f"Total maletas (4 semanas): {total_maletas}")
            print(f"Promedio diario: {promedio_diario:.2f}")
            print(f"Días con exceso (> {umbral_diario} maletas): {dias_exceso}")
            print(f"Pago total recibido: ${total_pago}")
        case "S":
            e = False
        case _:
            print("Modo no valido, dele bien")
GH = 12000
PA = 276800
VC = 0.70
e = True

while e:
    print("C. Calcular Rentabilidad de vuelo\nS. Salir")
    O = input("elija una opcion: ").upper()
    match O:
        case "C":
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
        case "S":
            e = False
        case _:
            print("Modo no valido, dele bien")
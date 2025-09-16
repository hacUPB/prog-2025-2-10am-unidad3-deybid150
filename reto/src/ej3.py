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

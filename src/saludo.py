print("¿como te llamas(nombre y apellido)")
nombre = input()
print ("bienvenido: ", nombre)

#calcular el IMC de esa persona
peso = input ("ingresa tu peso en kilogramos: ")
peso = float(peso)
altura = input ("ingresa tu estatura en metros: ")
altura = float(altura)
IMC = peso/altura**2

if IMC < 18.5:
    estatus = "desnutricion tipo guajira"
elif 18.5 < IMC < 24.9:
        estatus = "normal"
elif 25 < IMC < 29.9:
            estatus = "sobre peso" 
elif 30 < IMC < 34.9:
                estatus = "obesidad 1"
elif 35 < IMC < 39.9:
                    estatus = "obesidad 2"
elif IMC >= 40:
                        estatus = "obesidad extrema 3"
print(f" {nombre}, tu IMC es igual a: {IMC:0.2f}, tu estatus es: {estatus}")





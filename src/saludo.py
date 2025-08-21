print("¿como te llamas(nombre y apellido)")
nombre = input()
print ("bienvenido: ", nombre)

#calcular el IMC de esa persona
peso = input ("ingresa tu peso en kilogramos: ")
peso = float(peso)
altura = input ("ingresa tu estatura en metros: ")
altura = float(altura)
IMC = peso/altura**2

if 18.5 < IMC < 24.9:
    estatus = "normal"
else:
    if 25 < IMC < 29.9:
        estatus = "sobre peso" 
    else:
        if 30 < IMC < 34.9:
            estatus = "obesidad 1"
        else: 
            if 35 < IMC < 39.9:
                estatus = "obesidad 2"
            else:
                if IMC >= 40:
                    estatus = "obesidad extrema 3"

print(nombre, "tu IMC es igual a: ", IMC, "tu estatus es: ", estatus)

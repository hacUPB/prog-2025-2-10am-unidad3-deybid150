print("¿como te llamas(nombre y apellido)")
nombre = input()
print ("bienvenido: ", nombre)

#calcular el IMC de esa persona
peso = input ("ingresa tu peso en kilogramos: ")
peso = float(peso)
altura = input ("ingresa tu estatura en metros: ")
altura = float(altura)
IMC = peso/altura**2

print(nombre, "tu IMC es igual a: ", IMC)

#par o impar
numero = int(input("ingrese el numero entero"))
residuo = numero % 2
if residuo == 0:
    print(numero, "es par")
else: 
     print(numero, "es impar")
'''
se le pide al usuario que ingrese un numero entero y 
que muestre un mensaje si el numero es divisible por 3
'''
print("ingresa un numero")
numero = int(input())
residuo = numero % 3
if residuo == 0:
    print(f"{numero} es divisible entre 3")
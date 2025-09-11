'''
numero = 100
while numero >= 0:
    print(numero)
    numero -= 5
'''

NI = int(input("ingrese un numero de inicio entero "))
NF = int(input("ingrese numero final entero "))
while NI <= NF:
    residuo = NI % 2
    if residuo == 0:
        print(NI)
        NI += 2
    else:
        NI += 1

'''
for cont in range(1,20,3):
    print(cont)
'''

n = int(input("ingrese un numero"))
while n <= 0:
    n = int(input("ingrese un numero"))
    
    i = 0
    for cont in range(1, n+ 1):
        if cont % 2 == 0:
            i += cont
    print(f"la suma de los pares es: {i}")

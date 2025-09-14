n = int(input("ingrese un numero entero positivo: "))
i = 0
if n > 1:
    for p in range(1,n+1):
        if n % p == 0:
            i += 1
    if i == 1:
        print(f"{n} es primo")
    else:
        print(f"los divisores de {n} son:")
        for p in range(1,n+1):
            if n % p == 0:
                print(p)
elif n == 1:
    print("el 1 es primo")
elif n < 1:
    print("opcion no valida")
numero = int(input("ingrese el numero limite de la secuencia"))
if numero <= 0:
    print("por favor, ingrese un numero entero positivo")
elif numero == 1:
    print("serie de fibonacci: ")
    print(0)
else:
    a = 0
    b = 1
    i = 2
    print("serie de fibonacci")
    print(a)
    print(b)
    while i < numero:
        siguiente = a + b
        print (siguiente)
        a = b
        b = siguiente
        i += 1

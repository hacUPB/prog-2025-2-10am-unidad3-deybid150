<<<<<<< HEAD
# Análisis propuestas del RETO:

1. **Se consulta el precio de un vuelo de un A380 para una aerolinea, se necesita identificar el gasto del viaje en base a la variacion del peso en el vuelo por gasto de combustible y la distancia que recorre el avión. Para luego hacer una comparación de la venta de tiquetes y los gastos en combustible y confirmar si el vuelo es rentable para la aerolínea o no.**

## Análisis

**variables de entrada**
|nombre|tipo|comentario|
|--------------------|----|----------|
|CC|float|cantidad de combustible|
|NT|int|el numero de asientos vendidos|
|T|float|Tiempo de vuelo que recorre el avion|
|VT|float|valor del tiquete|

**constantes**
|nombre|tipo|comentario|valor|
|------|----|----------|-----|
|PA|float|peso de la aeronave|276.800 kg|
|GH|float|gasto de combustible por hora|12,000kg|
|VC|float|precio del combustible por kilogramo|US$ 0,70|

**variables de control**
|nombre|tipo|comentario|
|------|----|----------|
|H|int|hora de vuelo|
|e|booleana|determina si sale o no del menu|
|O|int|define el menu y sus opciones|

**variables intermedias**
|nombre|tipo|comentario|
|------|----|----------|
|P|float|peso|peso total de la aeronave cada hora|
|ST|float|la suma de los tiquetes vendidos|
|VV|float|Costo toatl del combustible|

**variables de salida**
|nombre|tipo|comentario|
|------|----|----------|
|viabilidad|STR|determina si es viable o no|
|G|float|ganancia o perdida|

## Pseudocódigo
```
INICIO
    DEFINIR GH = 12000        
    DEFINIR PA = 276800       
    DEFINIR VC = 0.70         
    DEFINIR e = VERDADERO

    MIENTRAS e = VERDADERO HACER
        MOSTRAR "C. Calcular rentabilidad de vuelo"
        MOSTRAR "S. Salir"
        LEER O
        CONVERTIR O A MAYÚSCULA

        SEGUN O HACER
            CASO "C":
                h ← 0
                LEER CC (cantidad de combustible en kg, entre 40.000 y 254.000)
                SI CC ES VÁLIDO ENTONCES
                    LEER NT (número de tickets vendidos, máximo 853)
                    SI NT ES VÁLIDO ENTONCES
                        LEER VT (precio de ticket, entre 400 y 1500)
                        SI VT ES VÁLIDO ENTONCES
                            LEER T (duración del vuelo en horas, entre 2 y 16)
                            SI T ES VÁLIDO ENTONCES
                                ST = NT * VT             
                                VV = CC * VC              
                                G = ST - VV               

                                MIENTRAS h < T HACER
                                    CC = CC - GH         
                                    h = h + 1
                                    SI CC <= 0 ENTONCES
                                        MOSTRAR "Vuelo inviable, sin combustible en hora", h
                                        MOSTRAR "Pérdida:", G
                                        SALIR DEL BUCLE
                                    FIN SI
                                FIN MIENTRAS

                                SI CC > 0 ENTONCES
                                    SI G < 0 ENTONCES
                                        MOSTRAR "Vuelo no rentable. Pérdida:", G
                                    SINO
                                        MOSTRAR "Vuelo rentable. Ganancia:", G
                                    FIN SI
                                FIN SI
                            SINO
                                MOSTRAR "Duración no permitida"
                            FIN SI
                        SINO
                            MOSTRAR "Precio no válido"
                        FIN SI
                    SINO
                        MOSTRAR "Número de asientos inválido"
                    FIN SI
                SINO
                    MOSTRAR "Cantidad de combustible no válida"
                FIN SI
            CASO "S":
                e ← FALSO
            CASO OTRO:
                MOSTRAR "Modo no válido"
        FIN SEGUN
    FIN MIENTRAS
FIN

#aqui se uso la IA para mostrar la hora y la perdida resultante de no completar el vuelo por falta de combustible  

```

2. **Se requiere hacer el registro del mantenimiento de la aeronave de tipo A350-900 para poder autorizar su operación. A dichas aeronaves se les debe hacer un chequeo de mantenimiento del sistema hidráulico cada 600 horas de vuelo, y del sistema eléctrico, cada 400 horas, y además del sistema de aire acondicionado. Si hay una falla en el sistema hidráulico se debe hacer una reparación frenando la operación 2 días, en el sistema eléctrico de 3 días, pero si hay una falla en el sistema de aire acondicionado, el avión puede operar, pero con la restricción de volar hasta los 10.000 pies.**

## Análisis

| Variable | Tipo de Variable | Comentario |
|----------|------------------|------------|
|horas_vuelo |Entrada |Valor ingresado que determina si se debe hacer un mantenimiento de dicho sistema. |
|sistema_H |Entrada |Se indica si el sistema hidráulico tiene una falla o está bien. |
|sistema_E |Entrada |Se indica si el sistema eléctrico tiene una falla o está bien. |
|sistema_A |Entrada |Se indica si el sistema de aire acondicionado tiene una falla o está bien. |
|autorización |Salida | Decide si se autoriza, se restringe o se autoriza con restricciones la operación de la aeronave. |

## Pseudocódigo
```
Inicio
Ingresar horas_vuelo 
   LEER horas_vuelo
   SI horasVuelo >= 600 ENTONCES
       MOSTRAR "Debe realizarse chequeo de mantenimiento al sistema hidráulico."
   FIN SI
   SI horasVuelo >= 400 ENTONCES
       MOSTRAR "Debe realizarse chequeo de mantenimiento al sistema eléctrico."
   FIN SI
   MOSTRAR "Debe realizarse chequeo de mantenimiento al sistema de aire acondicionado."
   LEER sistema_H   
   LEER sistema_E   
   LEER sistema_A   
   SI sistema_H = "FALLA" ENTONCES
       MOSTRAR "Reparación de sistema hidráulico: operación detenida por 2 días."
       autorizacionOperacion = "NO AUTORIZADA"
   SINO
 SI sistema_E = "FALLA" ENTONCES
       MOSTRAR "Reparación de sistema eléctrico: operación detenida por 3 días."
       autorización = "NO AUTORIZADA"
   SINO
 SI sistema_A = "FALLA" ENTONCES
       MOSTRAR "Falla en sistema de aire acondicionado: operación restringida a 10.000 pies."
       autorización = "AUTORIZADA CON RESTRICCIÓN"
   SINO
       MOSTRAR "Todos los sistemas están bien."
       autorización = "AUTORIZADA"
   FIN SI
   MOSTRAR "Estado final de la aeronave: ", autorización
FIN
```


3. Una empresa de cohetería desea analizar el rendimiento de un prototipo que recién desarrollaron para verificar si el consumo de combustible le permite alcanzar la altitud objetivo de 200 km, o si falla en alguna de las dos etapas de ascenso. En la primera etapa el cohete consume 800 kg/min de combustible y asciende 5km, mientras que en la segunda etapa el consumo es de 500 kg/min y asciende 3km.

## Análisis
 
| Variable | Tipo de Variable | Comentario |
|----------|------------------|------------|
|combustible_e1 |Entrada |Cantidad de combustible inicial de la etapa 1. |
|combustible_e2 |Entrada |Cantidad de combustible inicial de la etapa 2. |
|altitud |Proceso |Altitud alcanzada por minuto |
|min |Control | Cuenta minuto a minuto |
|etapa |Control |Determina si el cohete está en etapa 1 o 2. |
|resultado |Salida |Indica si logró alcanzar la altitud de 200km o falló. |

## Pseudocódigo
```
Inicio
    ojetivo_alt = 200
    consumo_1 = 800
    consumo_2 = 500
    IA1 = 5
    IA2 = 3
 
    Leer combustible_e1
    Leer combustible_e2
 
    altitud = 0
    minuto = 0
    etapa = 1
 
    Mientras altitud < objetivo_alt
        Si etapa = 1 Entonces
            Si combustible_e1 > 0 Entonces
                combustible_e1 = combustible_e1 - consumo_1
                altitud = altitud + IA1
                minuto ← minuto + 1
            Sino
                etapa = 2
            Fin Si
        Sino Si etapa = 2 Entonces
            Si combustible_e2 > 0 Entonces
                combustible_e2 = combustible_e2 - consumo_2
                altitud = altitud + IA2
                minuto = minuto + 1
            Sino
                Mostrar "El cohete se quedó sin combustible en la etapa 2."
                Mostrar "Altitud:", altitud
            Fin Si
        Fin Si
    Fin Mientras
 
    Si altitud >= objetivo_alt Entonces
        Mostrar "el cohete alcanzó la órbita de 200 km en", minuto, "minutos."
    Fin Si
Fin
 
```
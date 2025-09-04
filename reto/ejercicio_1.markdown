**Ejercicio 1** 
1. Se consulta el precio de un vuelo para una aerolinea, se necesita identificar el gasto del viaje en base a la variacion del peso en el vuelo por gasto de combustible y la distancia que recorre el avión. Para luego hacer una comparación de la venta de tiquetes y los gastos en combustible y confirmar si el vuelo es rentable para la aerolínea o no. 

**Tabla de analisis**

**variables de entrada**
|nombre|tipo|comentario|
|--------------------|----|----------|
|PI|float|peso inicial de la aeronave|
|CC|float|cantidad de combustible|
|NT|int|el numero de asientos vendidos|
|D|float|la distancia que recorre el avion|

**variables de control**
|nombre|tipo|comentario|
|------|----|----------|
|VT|float|valor del tiquete|
|PC|float|peso del combustible|
|P|float|peso|peso a medida que recorre distancia|
|VC|float|precio del combustible|
|VV|float|precio del viaje en base al combustible|
|ST|float|la suma de los tiquetes vendidos|

**variables de salida**
|nombre|tipo|comentario|
|------|----|----------|
|R|float|la rentabilidad o perdida resultante|
|E|booleana|determina si es viable o no|

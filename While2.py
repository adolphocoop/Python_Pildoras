import math
print("Programa de calculo de raiz cuadrada")

numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero<0:
#1. Hemos ingresado un valor negativo por lo que ha impreso la siguiente linea
    print("No se puede hallar la raiz de un numero negativo")
#2. No ha ingresado al primer if porque no vale 2
    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
#Al ingresar 3 veces un numero negativo se ejecutara el break saliendo del flujo hacia el siguiente if
        break
    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
#3. no ha incrementado la variable intentos hasta que se vuelva ingresar un numero
        intentos=intentos+1
#4. Como la variable intentos vale 2 y el siguiente if nos dice que que debe ser menor a 2 y es igual, salta el if y termina el programa

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))


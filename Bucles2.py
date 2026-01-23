#End se utiliza para imprimir todas las lineas en una sola

"""Vamos a evaluar si la direccion de correo es correcta
al tener arroba
"""


email= False
miEmail=input("Introduce tu direccion de email: ")

#La variable i va tomando  cada vuelta del bucle el valor del string

# Ejemplo: for i in "adolphovt12gmail.com":
for i in miEmail:
    if(i=="@" and i=="."):
        email=True

#La variable email al iniciar el bucle tiene el estado de falso
#Al momento en el que haya la "@" cambia su estado a True



# if email==True puede simplificarse como se muestra enseguida

"""
== Comparando una variable o mas
= asigna el valor a una variable
"""

if email:
    print("Email es correcto")
else:
    print("El email no es correcto")
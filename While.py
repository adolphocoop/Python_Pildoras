edad=int(input("Introduce tu edad por favor: "))

while edad<=5 or edad>100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo por favor")
    edad=int(input("Introduce tu edad por favor: "))

print("Gracias por participar")
print("La edad del aspirante es de " + str(edad))
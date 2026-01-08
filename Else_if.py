#Imprimimos el siguiente mensaje

#preguntamos la edad al usuario por teclado
edad_usuario=int(input("Introduce la edad por favor: "))

#Evaluar si la edad es mayor a 18

if edad_usuario<18:
    print("No puedes pasar")
elif edad_usuario>100:
    print("Edad fuera de rango")
else:
    print("Tienes acceso")

print("El programa ha finalizado")

#Pendiente min 10
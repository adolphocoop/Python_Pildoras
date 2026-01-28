valido = False


email=input("Introduce tu email: ")

#Devuelve la longitud del string, como esta dentro del range
#lo que nos devuelve el numero de elemntos, las vueltas del bucle
#
for i in range(len(email)):

    if email[i]=="@":
        valido=True

if valido:
    print("Email correcto")
else:
    print("El email es incorrecto")
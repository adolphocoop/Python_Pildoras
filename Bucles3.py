
#Iniciamos en cero 
contador=0
miEmail=input('Introduce tu direccion de email: ')

for i in miEmail:
    if(i=="@" or i==".")
#En el caso de que sencuentre la "@" valdra 1 y si encuentra el "." valdra 2
    contador=contador+1
#si contador vale 2
if contador ==2:
    print("Email es corecto")
else:
    print("El email no es correcto")
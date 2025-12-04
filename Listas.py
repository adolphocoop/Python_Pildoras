miLista=["Maria", "kasandra", "Daniela", "Melissa Perez"]
#append funciona para agregar algo a la lista 

miLista.append("Sandra")
#para usar insert debemos indicar el indice donde se agregara el otro elemento
miLista.insert(2,"Andrea mamita")
#Extend es una concatenacion agregamos mas elementos

miLista.extend(["Mayra", "Pamela", "Fany"])

#Para acceder a un indice en especifico ponemos el numero entre corchetes
#para comprobar si un elemento se encuentra
#print("Pepe" in miLista)
#Eliminacion de elementos
#miLista.remove("Anna")

print(miLista.index("Andrea mamita"))


#cuando introducimos un indice nagativo dara la vuelta a la lista

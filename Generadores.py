"""
Sintaxis:
Def generaNumeros():
   yield numeros

"""

#Genera lista de numeros pares
#el argumento limite, limitar el numero sin que sea infinito

def generaPares(limite):
    #Creamos una variable y se iguala 1
    num=1
    
    #lista donde se van almacenar los pares 

    while num<limite:
        yield num*2
        num=num+1
devuelvepares=generaPares(20)

#Recorremos el objeto iterable con un For

"""for i in devuelvepares:
    print(i)
"""
print(next(devuelvepares))
print("Aqui podria ir mas codigo")
print(next(devuelvepares))
print("Aqui podria ir mas codigo")
print(next(devuelvepares))
print("Aqui podria ir mas codigo")
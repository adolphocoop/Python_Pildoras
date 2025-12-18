
print("Programa de evaluacion de notas de alumno")

#El programa esta a la espera para introducir un dato, se almacena en nota alumno

nota_alumno=int(input("Ingresa la calificacion: "))
#El valor entra en la variable nota
def evalucaion (nota):
    valoracion="Aprobado"

    #Evaluar si la nota es menor que cinco y devolver el resultado
    if nota <=5:
        valoracion="Suspenso"
    return valoracion

#Llamamos a la funcion desde el print, el dato intrducio anteriormente
#en la variable nota alumno pasara a almacenarse en "nota" y como el print esta llamando a la funcion
#ejecutara el contedio de la funcion
print(evalucaion(nota_alumno))
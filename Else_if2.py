print("Programa de notas de alumnos")

nota_alumno=int(input("introduce la nota por favor: "))

#Evaluar si es insuficiente <5, suficiente =5, bien=6

if nota_alumno<5:
    print("insuficiente")
elif nota_alumno<6:
    print("Suficiente")
elif nota_alumno<7:
    print("Bien")
elif nota_alumno<9:
    print("Notable")
else:
    print("Sobresaliente")
print("Asignaturas optativas del anio 2026")

print("Informatica grafica - Pruebas de software- Usabilidad y accesibilidad ")

#Creamos nuestra variable
opcion=input("Escribe la asignatura escogida ")
asignatura = opcion.lower()

#Eavluar si lo que se ha introducido por teclado haya sido

if asignatura in ("iformatica grafica", "pruebas de software", "usabilidad y accesibilidad "):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura escogida no esta contemplada")


#funciones lower, transforma a minusculas
#upper transforma a mayusculas 
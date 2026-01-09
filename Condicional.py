
#Condicionales

#Programa para evaluar el salario 

#En python no existe el switch, lo que se hace es una concatenacion de 

salario_presidente=int(input("Introduce el salario del presidente: "))
#python es fuertemente tipado, hace una distincionentre diferentes tipos de datos
print("Salario del presidente:  " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("Salario del director: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe de area: "))
print("Salario del jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("Salario del administrativo: " + str(salario_administrativo))


if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Hubo un problema, los salarios no son los correctos")

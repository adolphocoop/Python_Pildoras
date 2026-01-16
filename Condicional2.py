print("Programa de becas año 2026")

distancia_escuela=int(input("introduce la distancia a la que vives: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos que tienes: "))

salario_familiar=int(input("Ingresa el salario anual de tus padres: "))
print(salario_familiar)


if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tines derecho a beca")

else:
    print("no tienes derecho a beca")
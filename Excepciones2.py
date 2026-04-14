#Ejemplo de excepciones con una sola funcion


def divide():
    try:
       op1=(float(input("Introduce el primer numero: ")))
       op2=(float(input("Introduce el segundo numero: ")))
       print("La division es: " + str(op1/op2))
    except ValueError:
        print("El valor introduciod es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0! ")
    print("El calculo ha finzalizado")
divide()


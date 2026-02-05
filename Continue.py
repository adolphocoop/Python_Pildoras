#Veamos el comportamiento del continue

for letra in "Python":

    #si a cada ireacion se iguala a "h" no imprime la siguiente linea por lo
    #salta a la siguiente linea
    if letra=="h":
        continue
    print("Viendo la letra " + letra)
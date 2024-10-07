import pandas as pd
import numpy as np

#leer tabla
df = pd.read_csv("datosPerceptron.csv",delimiter=";")

bias = np.random.rand() #numero entre 0 y 1
w1 = 2*np.random.rand()-1 #numero entre -1 y 1
w2 = 2*np.random.rand()-1 #numero entre -1 y 1
w3 = 2*np.random.rand()-1 #numero entre -1 y 1

iteraciones = 0

x1 = df["X1"].values
x2 = df["X2"].values
x3 = df["X3"].values
come = df["COME"].values
numero_iteraciones = len(come)

print(f"Pesos iniciales\nPeso1:{w1}\nPeso2:{w2}\nPeso3:{w3}\nBias:{bias}\n")

def entrenamiento(bias,w1,w2,w3,iteraciones,x1,x2,x3,come,numero_iteraciones):
    errores = True
    while(errores):
        errores = False
        for i in range(numero_iteraciones):
            #print(f"Iteracion #{i}")
            #print(f"y = ({x1[i]}*{w1}) + ({x2[i]}*{w2}) + ({x3[i]}*{w3}) + {bias}")
            y = (x1[i]*w1) + (x2[i]*w2) + (x3[i]*w3) + bias

        #mostrar valor de y
            #print(f"y= {y}\n")

        #activacion
            if y > 0:
                y = 1
                errores = False
                #print("Como y>= 0, entonces, todo ok\n")

            else:
                y=(-1)
                #print("Como y< 0, entonces")

            #if y != come[i]:
            if y != (-1):
                #print("Se recalculan los pesos")
                errores = True
            #calcular el error
                error = (come[i] - y)

            #mostrar el error
                #print(f"error= {error}")

            #recalcular bias
                bias = bias * error

            #recalcular pesos
                w1 = w1 + (error * x1[i])
                w2 = w2 + (error * x2[i])
                w3 = w3 + (error * x3[i])
                iteraciones+=1

                #print(f"Nuevo peso1: {w1}")
                #print(f"Nuevo peso2: {w2}")
                #print(f"Nuevo peso3: {w3}")

            else:
                print("No hay que recalcular los pesos")
                break

    return (w1,w2,w3,iteraciones,bias)

#mostrar valores finales
w1,w2,w3,iteraciones,bias = entrenamiento(bias,w1,w2,w3,iteraciones,x1,x2,x3,come,numero_iteraciones)
print("Pesos finales")
print(f"Iteraciones realizadas: {numero_iteraciones}")
print(f"Peso 1: {w1}")
print(f"Peso 2: {w2}")
print(f"Peso 3: {w3}")
print(f"Bias: {bias}")
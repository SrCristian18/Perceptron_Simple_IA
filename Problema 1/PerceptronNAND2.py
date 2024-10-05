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


def entrenamiento(bias,w1,w2,w3,iteraciones,x1,x2,x3,come,numero_iteraciones):
    errores = True
    while(errores):
        errores = False
        for i in range(numero_iteraciones):
            y = (x1[i]*w1) + (x2[i]*w2) + (x3[i]*w3) + bias

            #activacion
            if y >= 0:
                y = 1
            else:
                y=0

            if y != come[i]:
                errore = True
                #calcular el error
                error = (come[i] - y)

                #recalcular bias
                bias = bias * error

                #recalcular pesos
                w1 = w1 + (error * x1[i])
                w2 = w2 + (error * x2[i])
                w3 = w3 + (error * x3[i])
                iteraciones+=1
                
    return (w1,w2,w3,iteraciones,bias)

#mostrar valores finales
w1,w2,w3,iteraciones,bias = entrenamiento(bias,w1,w2,w3,iteraciones,x1,x2,x3,come,numero_iteraciones)
print(f"Iteraciones {numero_iteraciones}")
print(f"Peso 1 {w1}")
print(f"Peso 2 {w2}")
print(f"Peso 3 {w3}")
print(f"Bias {bias}")

import random
import numpy as np
import matplotlib.pyplot as plt

class PerceptronPaloma:
    def __init__(self):
        self.pesos = [random.uniform(-1, 1) for _ in range(3)]
        self.bias = random.uniform(-1, 1)
        self.tasaAprendizaje = 0.1

    def funcionActivacion(self, suma):
        return 1 if suma > 0 else -1

    def entrenar(self, inputs, desired_outputs):
        errores_epoca = [] #añadido
        for iteraciones in range(100):  # Número de épocas de entrenamiento
            error = False
            error_total = 0 #añadido
            for i in range(len(inputs)):
                suma = np.dot(inputs[i], self.pesos) + self.bias
                output = self.funcionActivacion(suma)
                error = error or (output != desired_outputs[i])
                error_term = desired_outputs[i] - output

                # Corrected line: Element-wise multiplication using * operator
                self.pesos += self.tasaAprendizaje * error_term * np.array(inputs[i])
                self.bias += self.tasaAprendizaje * error_term

                #añadido
                error_total +=abs(error_term)
            errores_epoca.append(error_total)

            if not error:
                break
        return errores_epoca #añadido
    
    def mostrarValoresIniciales(self):
        print(f"Patrones de entrada: \n{entradas}")
        print(f"Patrones de salida esperados: \n{salidas}")
        print("Peso inicial:", self.pesos)
        print("Peso del Bias:", self.bias)

    def mostrarValoresFinales(self):
        print("Pesos finales:", self.pesos)
        print("Peso del Bias final:", self.bias)

if __name__ == "__main__":
    # Datos de entrenamiento para la puerta NAND
    entradas = [[1, 1, 1], 
              [1, 1, -1], 
              [1, -1, 1], 
              [1, -1, -1],
              [-1, 1, 1], 
              [-1, 1, -1], 
              [-1, -1, 1], 
              [-1, -1, -1]]
    
    salidas = [1, 1, 1, 1, 1, 1, 1, -1]

    # Crear el perceptrón
    perceptron = PerceptronPaloma()

    #Mostrar valores iniciales
    perceptron.mostrarValoresIniciales()

    # Entrenar el perceptrón
    errores_epoca = perceptron.entrenar(entradas, salidas)
    print("")

    # Mostrar pesos y bias finales
    perceptron.mostrarValoresFinales()

    # Gráfica de la disminución del error
    plt.plot(errores_epoca)
    plt.title('Error por épocas en entremamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Error total')
    plt.show()
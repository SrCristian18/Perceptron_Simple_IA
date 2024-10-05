import random
import numpy as np

class PerceptronNAND:
    def __init__(self, learning_rate=0.1):
        self.weights = [random.uniform(-1, 1) for _ in range(3)]
        self.bias = random.uniform(-1, 1)
        self.learning_rate = learning_rate

    def activation(self, sum):
        return 1 if sum > 0 else -1

    def train(self, inputs, desired_outputs):
        for epoch in range(100):  # Número de épocas de entrenamiento
            error = False
            for i in range(len(inputs)):
                sum = np.dot(inputs[i], self.weights) + self.bias
                output = self.activation(sum)
                error = error or (output != desired_outputs[i])
                error_term = desired_outputs[i] - output

                # Corrected line: Element-wise multiplication using * operator
                self.weights += self.learning_rate * error_term * np.array(inputs[i])
                self.bias += self.learning_rate * error_term

                if not error:
                    break

    def predict(self, inputs):
        sum = np.dot(inputs, self.weights) + self.bias
        return self.activation(sum)
    
    def show_weights_and_bias(self):
        print("Pesos finales:", self.weights)
        print("Bias final:", self.bias)

if __name__ == "__main__":
    # Datos de entrenamiento para la puerta NAND
    inputs = [[1, 1, 1], 
              [1, 1, -1], 
              [1, -1, 1], 
              [1, -1, -1],
              [-1, 1, 1], 
              [-1, 1, -1], 
              [-1, -1, 1], 
              [-1, -1, -1]]
    
    outputs = [1, 1, 1, 1, 1, 1, 1, -1]

    # Crear el perceptrón
    perceptron = PerceptronNAND()

    # Entrenar el perceptrón
    perceptron.train(inputs, outputs)

    # Mostrar pesos y bias finales
    perceptron.show_weights_and_bias()

    # Hacer una predicción
    new_input = [-1, -1, 1]
    prediction = perceptron.predict(new_input)
    print(f"Salida para {new_input}: {prediction}")
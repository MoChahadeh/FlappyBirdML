import numpy as np


def ReLU(Z):

    return np.maximum(Z, 0)

def softmax(Z):

    return np.exp(Z) / np.sum(np.exp(Z))

class NeuralNet():

    def __init__(self, i, h, o):

        self.W1 = np.random.rand(h, i) - 0.5
        self.b1 = np.random.rand(h, 1) - 0.5
        self.W2 = np.random.rand(o, h) - 0.5
        self.b2 = np.random.rand(o, 1) - 0.5
    
    def forward(self, inputs: list):

        Z1 = self.W1.dot(inputs) + self.b1
        A1 = ReLU(Z1)

        Z2 = self.W2.dot(A1) + self.b2
        A2 = softmax(Z2)

        return A2



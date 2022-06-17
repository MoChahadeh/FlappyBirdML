import numpy as np
from math import exp

from regex import P

def ReLU(Z):

    return np.maximum(0, Z )

def sigmoid(Z):

    return 1/(1+np.exp(-Z))

class NeuralNet():

    def __init__(self, i:int, h:int, o:int):

        self.W1:np.ndarray = np.random.rand(h, i) - 0.5
        self.b1:np.ndarray = np.random.rand(h, 1) - 0.5
        self.W2:np.ndarray = np.random.rand(o, h) -0.5
        self.b2:np.ndarray = np.random.rand(o,1) -0.5
    
    def forward(self, inputs: np.ndarray):

        Z1 = np.dot(self.W1,np.transpose(inputs)) + self.b1
        A1 = ReLU(Z1)

        Z2 = np.dot(self.W2, A1) + self.b2
        A2 = sigmoid(Z2)

        return A2
    
    def mutate(self, rate):
        W1r, W1c = self.W1.shape
        self.W1 = self.W1 + (self.W1 * (np.random.rand(W1r, W1c) - 0.5) / (0.5/rate))
        b1r, b1c = self.b1.shape
        self.b1 = self.b1 + (self.b1 * (np.random.rand(b1r, b1c) - 0.5) / (0.5/rate))
        W2r, W2c = self.W2.shape
        self.W2 = self.W2 + (self.W2 * (np.random.rand(W2r, W2c) - 0.5) / (0.5/rate))
        b2r, b2c = self.b2.shape
        self.b2 = self.b2 + (self.b2 * (np.random.rand(b2r, b2c) - 0.5) / (0.5/rate))



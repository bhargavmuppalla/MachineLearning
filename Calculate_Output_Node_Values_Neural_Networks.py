#code to find output node values

from math import tanh
from math import exp
import numpy as np

#weights array for hidden layer
W_x_z = ([0.7,1.2,0.95,2.3,0.89],
        [0.15,0.12,0.25,1.4,0.7],
        [0.27,0.6,0.32,1.7,0.21],
        [0.01,0.81,0.19,0.33,1.1])

#input Array
X = [0.1,0.2,0.3,0.4]

#A(i) values before applying activation function. A[0] = x[0] * W_x_z[0][0] + x[1] * W_x_z[1][0] + x[2] * W_x_z[2][0] + x[3] * W_x_z[3][0]
A_x_z = np.dot(X, W_x_z)


Z = []
# a) Applying ReLU activation function on hidden layer. ReLU is defined as max(0,x).
#for x in A_x_z:
#    Z.append(max(0,x))

# b) Applying Tanh activation function on hidden layer. Tanh is defined as tanh(x).
for x in A_x_z:
    Z.append(tanh(x))

#weights array for output layer
W_y_z = ([1.3,0.24,1.4],
        [0.37,1.5,0.67],
        [0.74,0.9,0.32],
        [0.46,0.48,0.1],
        [0.17,1.9,0.15])

#output values. Y[0] = Z[0] * W_y_z[0][0] + Z[1] * W_y_z[1][0] + Z[2] * W_y_z[2][0] + Z[3] * W_y_z[3][0]
Y = np.dot(Z, W_y_z)

# c), d) Applying softmax activation function to output values.
denominator = 0
for x in Y:
    denominator = denominator + exp(x)

for i in range(len(Y)):
    Y[i] = exp(Y[i]) / denominator

print(Y)

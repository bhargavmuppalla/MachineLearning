from math import tanh
from math import exp
import math
from operator import le
from traceback import print_list
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
#denominator = 0
#for x in Y:
#    denominator = denominator + exp(x)

#for i in range(len(Y)):
#    Y[i] = exp(Y[i]) / denominator

T = ([1,2,3])

#partial error of output nodes

po = Y - T
#print(po)

# 2.a) partial errors of hidden layer. since all z values are greater than 1 so. h`(x) = 1 for all.
#ph = 1 * np.dot(W_y_z,po)
#print(ph)


# 2.b) partial errors of hidden nodes. h`(a) = 1-tanh^2(x)
ph = []
for i in range(len(W_y_z)):
    temp = 0
    for j in range(len(W_y_z[0])):
        temp = temp + (W_y_z[i][j] * po[j]) 
    
    temp = temp * (1 - (math.tanh(A_x_z[j]) * math.tanh(A_x_z[j])))
    ph.append(temp)

#print(ph)



# 3. computing gradients for weights b/w hidden layer and output layer.
gradientOfWeightsH = []
for i in range(len(Z)):
    tempWeights = []
    for j in range(len(Y)):
        tempWeights.append(po[j]*Z[i])
    gradientOfWeightsH.append(tempWeights)

# updating weights b/w hidden layer and output layer
uW_y_z = np.subtract(W_y_z,gradientOfWeightsH);
#print(uW_y_z);

#computing gradients for weights b/w hidden layer and input layer.
gradientOfWeightsI = []
for i in range(len(X)):
    tempWeights = []
    for j in range(len(ph)):
        tempWeights.append(X[i]*ph[j])
    gradientOfWeightsI.append(tempWeights)

#print(gradientOfWeightsI)
#updating weights b/w hidden layer and input layer
uW_x_z = np.subtract(W_x_z,gradientOfWeightsI)
print(uW_x_z)

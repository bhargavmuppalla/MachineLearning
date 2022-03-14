#The following program classifies data based on the label. the label has either 0 or 1. 0 points are considered red points and 1 points are considered as blue.
#we draw a decision boundary after the classification

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.linear_model import RidgeClassifier
from sklearn import svm
data = np.loadtxt("/Users/bhargavmuppalla/Documents/Machine Learning/ML HW 2/Homework_2_Q1_Data.csv", delimiter=",")

x = data[:,0:2]
#y = data[:,1]
label = data[:,2]

# classification using ridgeclassifier
ridClf = RidgeClassifier().fit(x,label)
coeffs = ridClf.coef_
weights = []
#adding weight w2 
weights.append(coeffs[0][0])
#adding weight w1
weights.append(coeffs[0][1])
#adding weight w0
weights.append(ridClf.intercept_[0])
print(weights)

#distance from a point to a line is y(x)/||w||
#||W|| = sqrt(w2^2 + w1^2)


#y(x)
def lineEquation(x1,x2):
    return weights[0] * x1 + weights[1] * x2 + weights[2]

#||w||
w = np.sqrt(weights[0] **2 + weights[1] ** 2)


for i in range(len(x)):
    dist = lineEquation(x[i][0],x[i][1])/w
    print("distance of point (%f"%(x[i][0]),", %f"%(x[i][1]),") from Boundary is", dist)


colormap = np.array(['r','b'])
category=[]
for i in range(len(x)):
    if(label[i] == 0):
        category.append(0)
    elif(label[i] == 1):
        category.append(1)


plt.scatter(x[:,0],x[:,1],c=colormap[category])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Classifier")

xn = np.linspace(-0.8,0.8,100)
#yn = np.polyval(weights,xn)
# ridge classifier gives weights for w2 * x1 + w1 * x2/y + w0(intercept)
# for plotting we convert the equation to x2/y = (-w2/w1 * x1 - w0/w2)
lequ = -1 * (2.125746059120498/0.7124670554550044) * xn + -1 * (0.08280293041389122/0.7124670554550044)
plt.plot(xn,lequ,'black')
plt.show()

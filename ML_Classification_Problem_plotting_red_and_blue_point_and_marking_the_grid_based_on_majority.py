from unicodedata import category
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
from pyparsing import alphas

data = pd.read_csv('Homework_1_Q2_Data.csv',header=None)

"""
for bonus question
x = data[1]
y = data[3]
"""
x = data[2]
y = data[4]

colormap = np.array(['r','b'])
category=[]
for i in range (1,51):
    if(i%2 == 0):
        category.append(1)
    else:
        category.append(0)
#print(category)
fig = plt.figure()

ax = fig.add_subplot(1,1,1)

fig,ax=plt.subplots()
plt.scatter(x,y,c=colormap[category])

plt.xlim(0.0,1.0)
plt.ylim(0.0,1.0)
plt.xlabel("X3")
plt.ylabel("Y5")

ax.set_xticks([0.25,0.5,0.75,1.0], major=True)
ax.set_yticks([0.25,0.5,0.75,1.0], major=True)


ax.grid()


#uncomment this for 2 a,b
ax.axhspan(0.0,0.25,0.25,0.5,facecolor='red',alpha = 0.7)
ax.axhspan(0.0,0.25,0.5,0.75,facecolor='blue',alpha = 0.7)
ax.axhspan(0.0,0.25,0.75,1.0,facecolor='blue',alpha = 0.7)
ax.axhspan(0.25,0.5,0.25,0.5,facecolor='blue',alpha = 0.7)
ax.axhspan(0.25,0.5,0.75,1.0,facecolor='blue',alpha = 0.7)
ax.axhspan(0.5,0.75,0.0,0.25,facecolor='blue',alpha = 0.7)
ax.axhspan(0.5,0.75,0.5,0.75,facecolor='red',alpha = 0.7)
ax.axhspan(0.5,0.75,0.75,1.0,facecolor='blue',alpha = 0.7)
ax.axhspan(0.75,1.0,0.0,0.25,facecolor='red',alpha = 0.7)
ax.axhspan(0.75,1.0,0.5,0.75,facecolor='red',alpha = 0.7)
ax.axhspan(0.75,1.0,0.75,1.0,facecolor='red',alpha = 0.7)


"""
ax.axhspan(0.0,0.25,0.0,0.25,facecolor='blue',alpha = 0.7)
ax.axhspan(0.0,0.25,0.25,0.5,facecolor='red',alpha = 0.7)
ax.axhspan(0.0,0.25,0.5,0.75,facecolor='blue',alpha = 0.7)
ax.axhspan(0.0,0.25,0.75,1.0,facecolor='red',alpha = 0.7)
ax.axhspan(0.25,0.5,0.25,0.5,facecolor='blue',alpha = 0.7)
ax.axhspan(0.25,0.5,0.5,0.75,facecolor='red',alpha = 0.7)
ax.axhspan(0.25,0.5,0.75,1.0,facecolor='blue',alpha = 0.7)
ax.axhspan(0.5,0.75,0.5,0.75,facecolor='red',alpha = 0.7)
ax.axhspan(0.75,1.0,0.0,0.25,facecolor='blue',alpha = 0.7)
ax.axhspan(0.75,1.0,0.25,0.5,facecolor='red',alpha = 0.7)
ax.axhspan(0.75,1.0,0.5,0.75,facecolor='blue',alpha = 0.7)
ax.axhspan(0.75,1.0,0.75,1.0,facecolor='blue',alpha = 0.7)
"""
plt.show()
plt.close()

#print(x,y)
#print(data)


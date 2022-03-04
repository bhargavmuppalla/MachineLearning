
from numpy import array, exp, math, polyfit, random
import matplotlib.pyplot as plt 

x = array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
y = array([0.8750,0.0753,-0.7305,-0.5486,0.1903,1.0873,0.2081,-0.7886,-0.5698,0.3331,0.7926])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#1a answer
for i in range(2,10):
    pw = polyfit(x,y,i)
    print(i,"=",pw)


#1b answer
def f1(x):
    return -0.44355089 * x**3 + 3.26780886 * x**2 + -2.79809363 * x + 0.46130839

for i in range(len(x)):
    se = (y[i]-f1(x[i]))**2
    print("For x=%f"%(x[i]),"squared error = ",se)

data = []
for i in range(len(x)):
    data.append(f1(x[i]))

plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y)
ax.plot(x,data,'r')
plt.show()

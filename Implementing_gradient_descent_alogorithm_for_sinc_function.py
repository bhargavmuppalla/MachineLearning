import math

# 2) computing gradient
#d/dx(u/v) = (v*d/dx(u) - u. d/dx(v)) / v^2
# derivative of sin(pi * x)/pi * x = ( (pi*x) cos(pi * x) - sin(pi * x) * pi ) / (x^2) 
def sincDerivative(x):
    if(x != 0):
        derivative = -1 * math.sin(math.pi * x)/ (math.pi * (x ** 2)) + math.pi * (math.cos(math.pi * x))/ (math.pi * x)
    else:
        derivative = 0
    #print("derivative of : ",x)
    return derivative

# gradient computing function
def gradientDescent(initialValue, learningRate):
    
    # 1) setting initial value
    currentx = initialValue
    previousx = initialValue
    i=1

    # 3) looping till stop condition is reached
    while True:
        previousx = currentx
        currentx = previousx - abs(learningRate * sincDerivative(previousx))
        if(currentx >= previousx or currentx < 0.2 ):
            break
        
        print("x( %d"%i,") = %f"%currentx)
        i = i+1


# Taking initial value as user input
initialValue = float(input("Enter Intial Value : "))
learningRate = float(input("Enter learning Rate : "))

gradientDescent(initialValue,learningRate)

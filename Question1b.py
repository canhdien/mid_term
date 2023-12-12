import numpy as np
import matplotlib.pyplot as plt
import math as math
from sympy import symbols, Eq, solve
import sympy as sp

input = 45 # Use for A 
x,A= sp.symbols('x,A')# This part for finding the equation of tangent line
f = x**2 -(2*A)*x - A**2
def fm(x,A):
    return  x**2 -(2*A)*x  - A**2
df = sp.diff(f,x)
df1 = df.subs(A,input)
slope = df1.subs(x,0)
print(slope)
y_tangentLine = slope * (x) - (input **2)
def yline(x):
    return slope * (x) - (input **2)

#
xvalues = np.linspace(-1000,1000)
fvalues = fm(xvalues,input)
yvalues =yline(xvalues)
shift_ammount = 4*input**3
shifted_f= fvalues - shift_ammount
finter= fm(x,input)


#find the intersaction 
#intersaction = 0

def calculateIntersactionOnY(x):
    return slope*x-input
def f_shifted(x,A):
    return x**2 -(2*A)*x - A**2- 4*A**3
f4unit= f_shifted(x,input)
a1,b1,c1= 1,-2*input, -input**2-4*input**3
a2,b2,c2=0,-2*input, -input**2
result_a = a1-a2
result_b = b1-b2
result_c = c1-c2
intersaction_finres= result_a *x**2 + result_b*x + result_c 
d = (result_b**2) - (4*result_a*result_c)
root_1= (-result_b-math.sqrt(d))/(2*result_a)
root_2= (-result_b+math.sqrt(d))/(2*result_a) 
root_3 = f_shifted(root_1,input)
root_4 = f_shifted(root_2,input)

# intersaction1 = 0
# intersaction2 = -225
equation1= slope*x-input**2
equation2 = x**2 -2*input*x-input**2 
print(equation1)
# Set the equations equal to each other
equation = Eq(equation1, equation2)

# Solve for x
solution = solve(equation, x)
intersactionOnX = solution[0]
intersactionOnY = calculateIntersactionOnY(intersactionOnX)
print(solution)



print("Equation of the tangent line to the curve f(x) : ", y_tangentLine)
print(" 1b. Intersection point 1 :", ( root_1, root_3))
print(" 1b. Intersaction point 2 : ", (root_2,root_4))










#plot the function

plt.title("Question 1b")

plt.plot(xvalues, fvalues, label='f(x)')
plt.plot(xvalues ,yvalues, label =' tangent line to f(x)')
plt.plot(xvalues,shifted_f, label = ' shifted f(x)')
plt.scatter(intersactionOnX,intersactionOnY, color = 'red', label = " intersaction point")
plt.scatter(root_1,root_3,color = 'blue')
plt.scatter(root_2,root_4, color = 'blue')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()




#

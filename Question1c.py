import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, solve

input = 10 # Use for A
x, x0 = symbols('x x0')
fx = x**2 - 2*input*x - input**2
df = diff(fx, x)
slope = df.subs(x, x0)
y_tangentLine = slope * (x - x0) + fx.subs(x, x0)

moiGiaTri_x = solve(y_tangentLine.subs(x, 0) - (-4*input**3))
x1, x2 = float(moiGiaTri_x[0]), float(moiGiaTri_x[1])
y1, y2 = fx.subs(x, x1), fx.subs(x, x2)

print(f"Equation of the tangent line 1 to the curve f(x) : {y_tangentLine.subs(x0, x1)}")
print(f"Equation of the tangent line 2 to the curve f(x) :: {y_tangentLine.subs(x0, x2)}")

# Plot the function
x_values = np.arange(-100, 101)
def fx(x):
    return x**2 - 2 * input * x - input**2
def y_tangentLine1(x):
    return slope.subs(x0, x1) * (x - x1) + y1
def y_tangentLine2(x):
    return slope.subs(x0, x2) * (x - x2) + y2


plt.plot(x_values, fx(x_values), label='f(x)')
plt.plot(x_values, y_tangentLine1(x_values), label='tangent line 1')
plt.plot(x_values, y_tangentLine2(x_values), label='tangent line 2')
plt.scatter(0, -4*input**3, color='green')
plt.scatter(x1, y1, color='black')
plt.scatter(x2, y2, color='black')

plt.ylabel('y')
plt.xlabel('x')
plt.title("Question 1c")
plt.legend()
plt.show()
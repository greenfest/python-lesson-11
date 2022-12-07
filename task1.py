# Постройте график функции 𝑓(x)=5x^2+10x−30
# По графику определите, при каких значения x значение функции отрицательно.

import math
import matplotlib.pyplot as plt
import numpy as np


def GetRoots(a, b, c):
  dis = b * b - 4 * a * c 
  sqrt_val = math.sqrt(abs(dis)) 
      
  if dis > 0: 
      return (-b + sqrt_val)/(2 * a),(-b - sqrt_val)/(2 * a)
    
  elif dis == 0: 
      return -b / (2 * a)
    
  else:
      return (- b / (2 * a), " + i", sqrt_val),(- b / (2 * a), " - i", sqrt_val)


k1 = 5
k2 = 10
k3 = -30

roots = GetRoots(k1, k2, k3)
print(roots)

if isinstance(roots, tuple):
    x1, x2 = roots
    points = x1, x2
    y0 = 0, 0
    plt.scatter(points, y0, color='red')
else:
    x = roots
    points = x
    y0 = 0
    plt.scatter(points, y0, color='red')
 
 
freq = 100
a, b = -10, 10
 
xi = np.linspace(a, b, freq)
y = [k1 * t * t + k2 * t + k3 for t in xi]
plt.plot(xi, y)
 
 
plt.grid()
plt.show()
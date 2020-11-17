#Importando las librerías necesarias para graficar
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0.2,0.25,0.001)
def f(x):
  return 25*np.power(x,3)-26*np.power(x,2)+9*x-1

#print(f(1.25))
#print(f(1.75))
plt.plot(x,f(x))
plt.grid(bool)
ax=plt.gca()
ax.tick_params(axis='x', colors='red')
ax.tick_params(axis='y', colors='red')
ax.spines['bottom'].set_position(('data',0))
plt.show()

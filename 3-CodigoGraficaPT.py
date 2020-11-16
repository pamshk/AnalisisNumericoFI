import numpy as np
import matplotlib.pyplot as plt
 
x=np.arange(-2,4,0.1) #Rango de -2 a 4, en "saltos" de 0.1 unidades
def p(x): #definimos nuestra función obtenida
  return 1-np.power(x,2)/2+np.power(x,3)/24 
 
fo=np.cos(x)
 
plt.plot(x,p(x),label='Función aproximada o P(x)' )
plt.plot(x,fo,label='Función original f(x)')
plt.grid(bool)
plt.legend()
plt.show()

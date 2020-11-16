#Código para obtener el polinomio de Taylor

import numpy as np
import sympy as sym

x=sym.Symbol('x')
fx=sym.cos(x) 
x0=0  #Nuestro valor inicial
g=4   #Grado pedido en el problema 
n=g+1 # Términos de polinomio


k = 0 #Contador
polinomio = 0
while (k < n):
    dx=fx.diff(x,k)     #Se define la funcion derivada
    dx0=dx.subs(x,x0)   #derivada de 0
    divisor=np.math.factorial(k)
    terminok=(dx0/divisor)*(x-x0)**k
    polinomio=polinomio+terminok
    k=k+1 
    
print(polinomio)

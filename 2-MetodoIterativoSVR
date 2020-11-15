#Método iterativo sin valor real

from math import factorial

#Calculando el valor de e
e0=1/factorial(0) #nuestro valor inicial
print("Valor de e ", e0)
n=1 #contador

while True: #ciclo para iterar
  e1=e0+1/factorial(n)
  print("Valor aproximado de e: ", e1)
  Ea=abs(e0-e1)
  print("Error absoluto: ", Ea)
  Er=Ea/abs(e0)
  print("Error relativo: ", Er)
  Erp=Er*100
  print("Error relativo porcentual: ", Erp)
  e0=e1 #mi e0 ahora vale lo que mi e1
  n=n+1 #o en su defecto utilizar n+=1
  if Erp < 1.5: #tolerancia a manejar para el cierre del ciclo
    break
    
  

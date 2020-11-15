from math import factorial

#Calculando el valor de e

VR=2.71828
e=0 #Este es nuestro valor inicial

for n in range (0,5): #nuestro contador irá desde 0 a 5 (rango 0-5), sin embargo, puedes dar el valor que gustes
  e=e+1/factorial(n)
  print("Valor aproximado de e: ", e)
  Ea=abs(VR-e)
  print("Error absoluto: ", Ea)
  Er=Ea-VR
  print("Error relativo: ", Er)
  Erp=Er*100
  print("Error relativo porcentual: ", Erp)

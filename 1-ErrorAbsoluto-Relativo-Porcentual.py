#Notación cientifica en Python
print(1e3) #1x10^3
print(2.5e3) # ->2500

#Declaramos variables
Viga = 1000 #10 metros
VigaAproximada = 1050 # medida aproximada

#Se obtiene el error absoluto con la formula
#Error Absoluto = |(Valor Real - Valor aproximado)|
EA = abs(viga - vigaAproximada)
print("El error absoluto es: ", EA)

#Obtenemos el error relativo
ER = EA / abs(viga)
print("El Error relativo es:", ER)

#Obtenemos el error porcentual 
ERP = ER *100
print("El error Relativo Porcentual es", ERP)

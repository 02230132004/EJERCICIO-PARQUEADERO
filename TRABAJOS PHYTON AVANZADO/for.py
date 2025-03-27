# ******************* Tomar datos *******************

suma = 0  


print("Digite la cantidad de números para sumar: ")
cantidad = int(input())  

# ******************* Procesar datos *******************

for i in range(cantidad):
    print("Digite el número " + str(i + 1) + ": ") 
    numero = int(input()) 
    suma = suma + numero  

# ******************* Imprimir datos *******************

print("La sumatoria total es: " + str(suma))

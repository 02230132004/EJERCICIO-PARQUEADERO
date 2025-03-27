# ******************* Tomar datos *******************

print("Digite un número: ")
numero = int(input())  # Convertir la entrada en un número entero

# ******************* Procesar datos ****************

if numero > 0:
    resultado = "El número es positivo."
elif numero == 0:
    resultado = "El número es neutro."
else:
    resultado = "El número es negativo."

# ******************* Imprimir datos ****************

print(resultado)

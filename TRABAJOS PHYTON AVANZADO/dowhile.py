# ******************* Tomar datos *******************

while True:
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catálogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para salir del programa")

    # Leer la opción del usuario y convertirla en cadena
    letra = str(input())

    # ******************* Procesar datos *******************
   
    if letra == 'S' or letra == 's':
        print("Finalizó con éxito \n")  
        break 

    # ******************* Imprimir datos *******************
    
    else:
        print("Sigue dentro del proceso del DO WHILE \n")


print("EL DO-WHILE ha finalizado \n")

matriz = []
for i in range(30):
    matriz.append(["", "", "", 0, 0, 0])

total = 0
opcion = "0"

while opcion != "5":
    print("\n========================================")
    print("   SISTEMA DE REGISTRO DEL TALLER")
    print("========================================")
    print("1. Ingresar vehículo a reparación")
    print("2. Registrar salida de vehículo")
    print("3. Reporte de vehículos terminados")
    print("4. Reporte de todos los vehículos")
    print("5. Salir del sistema")
    print("========================================")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        if total >= 30:
            print("Límite alcanzado: El taller está lleno")
        else:
            matriz[total][0] = input("Placa: ")
            matriz[total][1] = input("Propietario: ")
            matriz[total][2] = input("Celular: ")
            matriz[total][3] = int(input("Día de ingreso (1-31): "))
            
            while matriz[total][3] < 1 or matriz[total][3] > 31:
                matriz[total][3] = int(input("Error. Día (1-31): "))
            
            total = total + 1
            print("Vehículo registrado exitosamente")
            
    elif opcion == "2":
        placa = input("\nPlaca a entregar: ")
        encontrado = 0
        
        for i in range(total):
            if matriz[i][0] == placa:
                encontrado = 1
                if matriz[i][4] != 0:
                    print("Este vehículo ya fue entregado")
                else:
                    matriz[i][4] = int(input("Día de salida: "))
                    
                    while matriz[i][4] < matriz[i][3] or matriz[i][4] > 31:
                        matriz[i][4] = int(input("Error. Día inválido: "))
                    
                    matriz[i][5] = matriz[i][4] - matriz[i][3]
                    print("Salida registrada. Demora: " + str(matriz[i][5]) + " días")
                break
                
        if encontrado == 0:
            print("Placa no encontrada")
            
    elif opcion == "3":
        print("\n--- REPORTE: VEHÍCULOS TERMINADOS ---")
        term = 0
        for i in range(total):
            if matriz[i][4] != 0:
                term = term + 1
                print("Placa: " + matriz[i][0] + " | Días demora: " + str(matriz[i][5]))
        print("Total terminados: " + str(term))
            
    elif opcion == "4":
        print("\n--- REPORTE: TODOS LOS VEHÍCULOS INGRESADOS ---")
        for i in range(total):
            print("Placa: " + matriz[i][0] + " | Prop: " + matriz[i][1] + " | Cel: " + matriz[i][2])
        print("Total ingresados: " + str(total))
            
    elif opcion == "5":
        print("Cerrando el sistema...")
        
    else:
        print("Opción inválida")
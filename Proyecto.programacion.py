
#Sunday 24 march 2024 10:00 AM
#-Alejandro Jair Estrada Pérez- 
#-------------P_E_N_S_A_M_I_E_N_T_O---------C_O_M_P_U_T_A_C_I_O_N_A_L--------------

#El código del “cajero calculadora” es un programa que simula una calculadora interactiva. Su 
#función es permitir que el usuario elija entre 
#varias operaciones matemáticas, ingresar los valores necesarios y recibir como resultado el 
#cálculo solicitado. El programa está organizado en un menú de opciones, donde cada número corresponde 
#a una operación diferente (suma, resta, multiplicación, división, potencia, raíz, multiplicar por PI, 
#módulo, porcentaje y descuento). Una vez elegida la opción, el  programa pide 
#los datos al usuario, realiza la operación con las fórmulas correctas y muestra el resultado. Este proceso 
#se repite hasta se pueda decidir
#Me parece importante ya que:
#- Se parece a un caso real, ya que cualquier persona podría usar una calculadora de este tipo para 
#resolver operaciones comunes.
#- Porque puede ser la base para proyectos más grandes, como una calculadora gráfica o alguna con mas digitos, 
#una app móvil o un sistema de facturación

#-----------------------------------ALGORITMO---------------------------------     
#ENTRADA:
#    Imprime esto en la pantalla:

#-------------------------ALGORITMO : CAJERO CALCULADORA--------------------     
#    Bienvenido al cajero de calculadora donde podras elegir entre estas opciones:
#        a - Suma
#        b - Resta
#        c - Multiplicación
#       d - División
#       e - Exponente (potencia)
#      f - Raíz cuadrada
#        g - Multiplicar por PI
#        h - Módulo (residuo de una división)
#        i - Porcentaje
#        j - Descuento
#        k - Salir
#    1. Elige un la opcion mediante la letra es el tipo de operacion
#    opcion=letra
       
     
# PROCESO:
#     2. Según la opción elegida:
#         2.1 Suma:
#             2.1.1_Pedir dos números (float) y sumarlos.
#         2.2 Resta:
#             2.2.1_Pedir dos números (float) y restarlos.
#         2.3 Multiplicación:
#             2.3.1_Pedir dos números (float) y multiplicarlos.
#         2.4 División:
#             2.4.1_Pedir dos números (float) y dividir el primero entre el segundo 
#             2.4.2_(si el segundo es distinto de 0).
#         2.5 Exponente:
#             2.5.1_Pedir la base y el exponente (float) y calcular base^exponente.
#         2.6 Raíz cuadrada:
#             2.6.1_Pedir un número (float) y calcular su raíz cuadrada si es  positivo.
#         2.7 Multiplicar por PI:
#             2.7.1_Pedir un número (float) y multiplicarlo por PI 3.141592.
#         2.8 Módulo:
#             2.8.1_Pedir dos números (int) y calcular el residuo de la división.
#         2.9 Porcentaje:
#             2.9.1_Pedir un número (float) y el porcentaje a calcular float.
#             2.9.2_Fórmula: resultado = número * (porcentaje / 100).
#         2.11 Descuento:
#             2.11.1_Pedir el precio original (float) y el porcentaje de descuento (float).
#             2.11.2_Fórmula: precio_final = precio_original - (precio_original * (descuento / 100)).
#         2.12 Salir:
#             2.12.1 Terminar el programa.
#     Si la opción no existe, mostrar un mensaje de error y volver a preguntar.
# SALIDA:
#     Mostrar el resultado de la operación.
#     Repetir el menú hasta que el usuario elija salir.

# Sunday 24 march 2024 10:00 AM
# -Alejandro Jair Estrada Pérez-
# -------------P_E_N_S_A_M_I_E_N_T_O---------C_O_M_P_U_T_A_C_I_O_N_A_L--------------
# ===============================================================
#      PROGRAMA: CAJERO CALCULADORA
#      Descripción: Calculadora interactiva que permite realizar
#      operaciones con números y matrices.
# ===============================================================

import math  # Se importa la librería math para funciones matemáticas (sqrt, pi, etc.)

# Mensaje de bienvenida
print("\n-------------------------ALGORITMO : CAJERO CALCULADORA--------------------")
print("Bienvenido al cajero de calculadora donde podrás elegir entre estas opciones:")

# ================= FUNCIONES ===================

# ---------- SUMA ----------
def suma():
    # El usuario elige si quiere sumar números o matrices
    tipo = input("¿Deseas sumar números simples o una matriz? (número/matriz): ").lower()

    if tipo == "número":
        # Pide la cantidad de números a sumar
        cantidad = int(input("¿Cuántos números deseas sumar? "))
        # Se crea una lista con los números ingresados
        numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(cantidad)]
        # Se usa la función sum() para obtener la suma total
        resultado = sum(numeros)
        print(f"La suma de {numeros} es: {resultado}")
        return resultado

    elif tipo == "matriz":
        # Llama a la función especial para sumar matrices
        return suma_matriz()

    else:
        print("Opción no válida.")
        return None


# ---------- RESTA ----------
def resta():
    tipo = input("¿Deseas restar números simples o matrices? (número/matriz): ").lower()

    if tipo == "número":
        cantidad = int(input("¿Cuántos números deseas restar? "))
        numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(cantidad)]
        # Se toma el primer número como base
        resultado = numeros[0]
        # Se restan los demás
        for num in numeros[1:]:
            resultado -= num
        print(f"La resta de {numeros} es: {resultado}")
        return resultado

    elif tipo == "matriz":
        return resta_matrices()

    else:
        print("Opción no válida.")
        return None


# ---------- MULTIPLICACIÓN ----------
def multiplicacion():
    tipo = input("¿Deseas multiplicar números simples o matrices? (número/matriz): ").lower()

    if tipo == "número":
        cantidad = int(input("¿Cuántos números deseas multiplicar? "))
        numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(cantidad)]
        # Se inicializa el resultado en 1 (neutro multiplicativo)
        resultado = 1
        for num in numeros:
            resultado *= num
        print(f"La multiplicación de {numeros} es: {resultado}")
        return resultado

    elif tipo == "matriz":
        return multiplicacion_matrices()

    else:
        print("Opción no válida.")
        return None


# ---------- SUMA DE MATRIZ ----------
def suma_matriz():
    filas = int(input("Número de filas de la matriz: "))
    columnas = int(input("Número de columnas de la matriz: "))
    # Crea la matriz pidiendo cada elemento
    matriz = [[float(input(f"Ingrese elemento [{i+1},{j+1}]: ")) for j in range(columnas)] for i in range(filas)]
    # Suma todos los elementos de la matriz
    resultado = sum(sum(fila) for fila in matriz)
    print(f"La matriz ingresada es: {matriz}")
    print(f"La suma de todos los elementos es: {resultado}")
    return resultado


# ---------- RESTA DE MATRICES ----------
def resta_matrices():
    filas = int(input("Número de filas de la matriz: "))
    columnas = int(input("Número de columnas de la matriz: "))

    print("Ingrese la primera matriz:")
    matriz1 = [[float(input(f"Elemento [{i+1},{j+1}]: ")) for j in range(columnas)] for i in range(filas)]

    print("Ingrese la segunda matriz:")
    matriz2 = [[float(input(f"Elemento [{i+1},{j+1}]: ")) for j in range(columnas)] for i in range(filas)]

    # Se restan elemento por elemento ambas matrices
    resultado = [[matriz1[i][j] - matriz2[i][j] for j in range(columnas)] for i in range(filas)]

    print(f"Resultado de la resta: {resultado}")
    return resultado


# ---------- MULTIPLICACIÓN DE MATRICES ----------
def multiplicacion_matrices():
    # Se piden dimensiones de las dos matrices
    filas1 = int(input("Filas de la primera matriz: "))
    columnas1 = int(input("Columnas de la primera matriz: "))
    filas2 = int(input("Filas de la segunda matriz: "))
    columnas2 = int(input("Columnas de la segunda matriz: "))

    # Validación de compatibilidad para multiplicar
    if columnas1 != filas2:
        print("Error: columnas de la primera matriz deben ser igual a filas de la segunda.")
        return None

    # Se capturan ambas matrices
    print("Ingrese la primera matriz:")
    matriz1 = [[float(input(f"Elemento [{i+1},{j+1}]: ")) for j in range(columnas1)] for i in range(filas1)]
    print("Ingrese la segunda matriz:")
    matriz2 = [[float(input(f"Elemento [{i+1},{j+1}]: ")) for j in range(columnas2)] for i in range(filas2)]

    # Se realiza la multiplicación clásica de matrices
    resultado = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(columnas1)) for j in range(columnas2)] for i in range(filas1)]

    print(f"Resultado de la multiplicación: {resultado}")
    return resultado


# ---------- DIVISIÓN ----------
def division():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
        return resultado
    else:
        print("Error: No se puede dividir entre cero.")
        return None


# ---------- EXPONENTE ----------
def exponente():
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    resultado = base ** exponente
    print(f"El resultado de {base} elevado a {exponente} es: {resultado}")
    return resultado


# ---------- RAÍZ CUADRADA ----------
def raiz_cuadrada():
    num = float(input("Ingrese un número: "))
    if num >= 0:
        resultado = math.sqrt(num)
        print(f"La raíz cuadrada de {num} es: {resultado}")
        return resultado
    else:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        return None


# ---------- MULTIPLICAR POR PI ----------
def multiplicar_por_pi():
    num = float(input("Ingrese un número: "))
    resultado = num * math.pi
    print(f"El resultado de multiplicar {num} por PI es: {resultado}")
    return resultado


# ---------- RESIDUO (MÓDULO) ----------
def residuo():
    num1 = int(input("Ingrese el primer número (dividendo): "))
    num2 = int(input("Ingrese el segundo número (divisor): "))
    if num2 != 0:
        resultado = num1 % num2
        print(f"El residuo de la división de {num1} entre {num2} es: {resultado}")
        return resultado
    else:
        print("Error: No se puede dividir entre cero.")
        return None


# ---------- PORCENTAJE ----------
def porcentaje():
    num = float(input("Ingrese un número: "))
    porcentaje = float(input("Ingrese el porcentaje a calcular: "))
    resultado = num * (porcentaje / 100)
    print(f"El {porcentaje}% de {num} es: {resultado}")
    return resultado


# ---------- DESCUENTO ----------
def descuento():
    precio_original = float(input("Ingrese el precio original: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))
    precio_final = precio_original - (precio_original * (descuento / 100))
    print(f"El precio final después de un descuento del {descuento}% es: {precio_final}")
    return precio_final


# ---------- SALIR ----------
def salir():
    print("Gracias por usar la maquina calculadora. ¡Hasta luego!")


# ================= MENÚ PRINCIPAL ===================
while True:
    # Se muestran todas las opciones disponibles
    print("\nMenú:")
    print("a - Suma")
    print("b - Resta")
    print("c - Multiplicación")
    print("d - División")
    print("e - Exponente")
    print("f - Raíz cuadrada")
    print("g - Multiplicar por PI")
    print("h - Módulo")
    print("i - Porcentaje")
    print("j - Descuento")
    print("k - Salir")

    # El usuario elige una opción
    opcion = input("\nSeleccione una opción: ").lower()

    # Estructura de control para ejecutar la función seleccionada
    if opcion == "a":
        suma()
    elif opcion == "b":
        resta()
    elif opcion == "c":
        multiplicacion()
    elif opcion == "d":
        division()
    elif opcion == "e":
        exponente()
    elif opcion == "f":
        raiz_cuadrada()
    elif opcion == "g":
        multiplicar_por_pi()
    elif opcion == "h":
        residuo()
    elif opcion == "i":
        porcentaje()
    elif opcion == "j":
        descuento()
    elif opcion == "k":
        print("Gracias por usar la calculadora. ¡Adiós!")
        break
    else:
        print("Opción no válida.")

    # Pregunta si el usuario quiere continuar
    continuar = input("\n¿Quieres hacer otra operación? (s/n): ").lower()
    if continuar != "s":
        print("Programa terminado. ¡Hasta luego!")
        break

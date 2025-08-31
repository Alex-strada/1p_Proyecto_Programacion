
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

import math

def mostrar_menu():
    print("\n-------------------------ALGORITMO : CAJERO CALCULADORA--------------------")
    print("Bienvenido al cajero de calculadora donde podrás elegir entre estas opciones:")
    print("   a - Suma")
    print("   b - Resta")
    print("   c - Multiplicación")
    print("   d - División")
    print("   e - Exponente (potencia)")
    print("   f - Raíz cuadrada")
    print("   g - Multiplicar por PI")
    print("   h - Módulo (residuo de una división)")
    print("   i - Porcentaje")
    print("   j - Descuento")
    print("   k - Salir")

def suma():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
    return resultado
def resta():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
    return resultado
def multiplicacion():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
    return resultado
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
def exponente():
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    resultado = base ** exponente
    print(f"El resultado de {base} elevado a {exponente} es: {resultado}")
    return resultado
def raiz_cuadrada():
    num = float(input("Ingrese un número: "))
    if num >= 0:
        resultado = math.sqrt(num)
        print(f"La raíz cuadrada de {num} es: {resultado}")
        return resultado
    else:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        return None
def multiplicar_por_pi():
    num = float(input("Ingrese un número: "))
    resultado = num * math.pi
    print(f"El resultado de multiplicar {num} por PI es: {resultado}")
    return resultado


# Aquí comenzaría el bucle principal para leer la opción y procesar operaciones
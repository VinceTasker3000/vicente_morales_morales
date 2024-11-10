# Módulo para poder usar funciones matemáticas
import math

# Función que mostrará un menú de opciones
def mostrar_menú():
    print("Menú de opciones:")
    print("1. Calcular el descuento por entradas al cine")
    print("2. Calcular área de un triángulo equilátero")
    print("3. Salir")

# Función para realizar el cálculo del descuento de las entradas de cine
def calcular_descuento(entradas):
    precio_base = 10
    if entradas >= 5:
        descuento = 0.25
    elif entradas >= 3:
        descuento = 0.15
    else:
        descuento = 0
    precio_final = entradas * precio_base * (1 - descuento)
    return precio_final

#Función para calcular el área de un triángulo equilátero
def calcular_area_triángulo(lado):
    area = (math.sqrt(3) * lado ** 2) / 4
    return area

# Esta función se encarga de que se ejecute el programa
def main():
    while True:
        mostrar_menú()
        opcion = input("Selecciona opción (1, 2, 3): ")

       # Dependiendo de la opción que se elija, se mostrará lo siguiente
        if opcion == '1':
            entradas = int(input("Ingresar número de entradas: "))
            precio_final = calcular_descuento(entradas)
            print(f"Precio final por {entradas} entradas es: ${precio_final:.2f}")
        elif opcion == '2':
            lado = float(input("Ingresar longitud del lado del triángulo equilátero: "))
            area = calcular_area_triángulo(lado)
            print(f"El área del triángulo equilátero es: {area:.2f}")
        elif opcion == '3':
            print("Cerrar programa")
            break
        else:
            print("No válido, seleccionar 1, 2 o 3.")

#Este es el punto de entrada del programa, llama a la función principal para iniciarlo
if __name__ == "__main__":
    main()

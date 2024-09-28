import math

def calcular_ecuacion_cuadratica(a, b, c):
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        # Dos soluciones reales y distintas
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return x1, x2
    elif discriminante == 0:
        # Una solución real (doble)
        x = -b / (2 * a)
        return x,
    else:
        # No hay soluciones reales
        return None

# Ejemplo de uso:
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

resultados = calcular_ecuacion_cuadratica(a, b, c)

if resultados is None:
    print("No hay soluciones reales.")
elif len(resultados) == 1:
    print(f"La solución doble es: {resultados[0]}")
else:
    print(f"Las soluciones son: x1 = {resultados[0]}, x2 = {resultados[1]}")

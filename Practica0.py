import math
# 1. Implementar en Python el proceso anterior, que use una función (externa implementada, o bien pasada como parámetro), que lea el x como parámetro y un n natural, y luego sobre el ex inicial aplique la f n veces, finalmente devolviendo el resultado obtenido tras la última aplicación.
def aplicar_funcion_reiteradamente(f, x, n):
    """
    Aplica la función f reiteradamente n veces al valor inicial x.
    
    Parámetros:
    f: función a aplicar
    x: valor inicial
    n: número de veces que se aplica la función
    
    Retorna:
    El resultado después de aplicar f n veces a x.
    """
    resultado = x
    for _ in range(n):
        resultado = f(resultado)
    return resultado

# Ejemplo 1: Función coseno
x_inicial = 1.0  # Valor inicial (en radianes)
n_veces = 10
resultado_cos = aplicar_funcion_reiteradamente(math.cos, x_inicial, n_veces)
#print(f"Aplicar coseno {n_veces} veces a {x_inicial}: {resultado_cos}")

# Ejemplo 2: Función f(x) = x^2 - 1
def f(x):
    return x**2 - 1

x_inicial = 5
n_veces = 10
resultado_cuad = aplicar_funcion_reiteradamente(f, x_inicial, n_veces)
#print(f"Aplicar f(x) = x^2 - 1 {n_veces} veces a {x_inicial}: {resultado_cuad}")

# 2. Implementar en Python un proceso al estilo del anterior, pero que use dos funciones, una f y una g, y que la aplicación iterada sea una vez f, luego g, luego f, luego g, y así siguiendo, alternando una con otra, en total las veces que se especifique por el parámetro n, y finalmente devuelva el resultado obtenido tras la última aplicación.
def aplicar_funciones_intercaladas(f1, f2, x, n):
    iterador = 0
    resultado = x
    for _ in range(n):
        if iterador == 0:
            resultado = f1(resultado)
            iterador = 1
        else:
            resultado = f2(resultado)
            iterador = 0
    return resultado

#print(f"Aplicar coseno y f(x) intercaladamente {n_veces} veces a {x_inicial}: {aplicar_funciones_intercaladas(math.cos, f, x_inicial, n_veces)}")

# 3. ¿Se le ocurre alguna forma de entender la idea de aplicar una f infinitas veces? ¿Cómo se podría definir esa aplicación infinitaria, y de qué dependerá que esté bien definida?
# La idea de aplicar una f infinitas veces se podría llegar a entender como una sumatoria ∑ x ∈ inf f(x). Pero necesitamos un epsilon para tener un límite de parada.

# 4. Aplicar el método de bisección para hallar una raíz aproximada de la función f(x) = x^3 + x - 5, comenzando con el intervalo [1,2], y el error epsilon = 0.5.
def biseccion_con_epsilon(f, a, b, epsilon):
    while (b - a >= epsilon):
        c = (a + b) / 2
        if (f(c) == 0):
            return c
        elif (sgn(f(c)) * sgn(f(a)) < 0):
            b = c
        else:
            a = c
    return c

def sgn(z):
    if (z == 0):
        return 0
    elif (z > 0):
        return 1
    else:
        return -1

def f1(x):
    return x**3 + x - 5

print(f"Bisección de f(x) = x^3 + x - 5 comenzando con el intervalo [1,2], y el error epsilon = 0.5 {biseccion_con_epsilon(f1, 1, 2, 0.5)}")

# 5. Aplicar el método de bisección para hallar una raíz aproximada de la función f(x) = x^3 + x - 10 haciendo 4 pasos.
def biseccion_con_pasos(f, a, b, n):
    for _ in range(n):
        c = (a + b) / 2
        if (f(c) == 0):
            return c
        elif (sgn(f(c)) * sgn(f(a)) < 0):
            b = c
        else:
            a = c
    return c

def f2(x):
    return x**3 +x - 10

print(f"Bisección de f(x) = x^3 + x - 10 haciendo 4 pasos: {biseccion_con_pasos(f2, 1, 2, 4)}")

# 6. Aplicar el método de bisección para hallar una aproximación de un x que cumpla x^2 + x = 12. Calcular luego el valor exacto de otra manera, y comparar.

def f3(x):
    return x**2 + x - 12

print(f"Bisección de f(x) = x^2 + x - 12: {biseccion_con_pasos(f3, 0, 5, 10)}")

# 7. Aplicar el método de bisección para aproximar un x que cumpla cos(x) = - 1/2, con error menor que epsilon = 1/10. Notar que esto sirve para encontrar aproximaciones de pi.

def f4(x):
    return (math.cos(x) + 1/2)

print(f"Bisección de f(x) = cos(x) + 1/2 con epsilon 1/10: {biseccion_con_epsilon(f4, 0, 8, 0.1)}")

# 8. Modificar la implementación del método de bisección para que:
# a) haga la menor cantidad posible de evaluaciones de la f en cada iteración
# b) vaya imprimiendo la secuencia de los puntos p que van aproximando a la raíz buscada
# c) que tenga una cota (grande) en la cantidad total de pasos que dará antes de devolver algo
# d) que devuelva, además del p encontrado, la cantidad de pasos que fueron necesarios para llegar a la aproximación buscad

def biseccion_con_epsilon(f, a, b, epsilon):
    pasos = 0
    while (b - a >= epsilon):
        pasos += 1
        fa = f(a)
        fb = f(b)
        c = (a + b) / 2
        fc = f(c)
        
        print(f"A: {a}")
        print(f"B: {b}")
        print(f"C: {c}")
        
        if (fc == 0):
            return c
        elif (sgn(fc) * sgn(fa) < 0):
            b = c
        else:
            a = c
        if(sgn(fa) * sgn(fb) >= 0):
            return f"No se encuentran raíces por método de bisección con estos puntos {a, b}"
    return c, pasos

# 9. Método de trisección. Implementar en Python un método para aproximar raíces al estilo de bisección, pero que en vez de dividir el intervalo en 2 subintervalos lo divida en 3, y en cada iteración elija uno de los 3 subintervalos que contenga una raíz. Usar una condición de parada análoga a la del método de bisección.
def triseccion_con_pasos(f, a, b, n):
    pasos = 0
    for _ in range(n):
        fa = f(a)
        fb = f(b)
        
        if(sgn(fa) * sgn(fb) >= 0):
            return f"No se encuentran raíces por método de bisección con estos puntos {a, b}"    
        
        pasos += 1
        r1 = abs(a - b) / 3 + min(a, b)
        r2 = abs(a - b) * 2 / 3 + min(a, b)
        fr1 = f(r1)
        fr2 = f(r2)
        
        if(fr1 == 0):
            return f"Raiz: {r1}"
        elif(fr2 == 0):
            return f"Raiz: {r2}"
        
        if(sgn(fa) * sgn(fr1) < 0):
            b = r1
        elif(sgn(fr1) * sgn(fr2) < 0):
            a = r1
            b = r2
        else:
            a = r2
    return (r1 + r2) / 2

print(f"Triceccion de f(x) = x^3 + x - 10 haciendo 20 pasos: {triseccion_con_pasos(f2, 0, 50, 20)}")
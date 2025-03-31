import sympy as sp
x = sp.symbols('x')

def f(x):
    return x**3 + x - 2

def iteracion():
    global x0
    x1 = x0 - f(x0) / sp.diff(f(x), x)
    x0 = x1
    return x1
    
def iterar(n):
    for i in range(n):
        raiz = iteracion()
    return raiz

x0 = 5  # Valor inicial
x_final = iterar(5)
print(f"\nResultado final: {x_final}")
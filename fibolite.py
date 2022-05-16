# Fibonacci Logarítmico
def fibonacci(n):
    # Auxiliar: Retorna T si n es un número par
    even = lambda n: (n % 2 == 0)

    (actual, siguiente, a,b) = (0, 1, 0, 1)    

    while (n > 0):
        if (even(n)):
            (a, b) = (a**2 + b**2, b**2 + 2*a*b)
            n /= 2
        else:
            (actual, siguiente) = (a*actual + b*siguiente, b*actual + (a+b)*siguiente)
            n -= 1
    
    return actual
print(fibonacci(15))
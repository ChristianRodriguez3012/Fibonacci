#Fibonacci 
#def fibonacci(n):
#    # Helper function: returns True if n is an even number.
#    even = lambda n: (n % 2 == 0)
#
#    (current, next, p, q) = (0, 1, 0, 1)    
#
#    while (n > 0):
#        if (even(n)):
#            (p, q) = (p**2 + q**2, q**2 + 2*p*q)
#            n /= 2
#        else:
#           (current, next) = (p*current + q*next, q*current + (p+q)*next)
#            n -= 1
    
#    return current


#Fibonacci MEMORIA
contenedor = {}
def Memoria_Fibonacci(num):
        if  (num < 2):
                return 1
        elif (num in contenedor):
                return contenedor[num]
        else:
                x = Memoria_Fibonacci(num - 1) + Memoria_Fibonacci(num - 2)
                contenedor[num] = x
                return x

#Corrigiendo el input del valor a calcular
Ingreso = (int(input("El orden a calcular: ")))
IngresoCorregido = Ingreso - 1
print(Memoria_Fibonacci(IngresoCorregido))


Print ("Fibonacci Iterativo")
def Iterativo_Fibonacci (Posicion, Out_Salida):
    Ejecuta_Ahora = 0
    Ejecuta_Despues = 1
    for i in range (Posicion + 1):
        if Out_Salida:
            print(str(Ejecuta_Ahora)+ ", ", end = "")
        Valor_Temporal = Ejecuta_Ahora
        Ejecuta_Ahora = Ejecuta_Despues
        Ejecuta_Despues = Ejecuta_Despues + Valor_Temporal
    return Valor_Temporal

Posicion = 10

print(f"Imprimiendo Fibonacci hasta {Posicion}")
Iterativo_Fibonacci(Posicion, True)
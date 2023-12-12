def fibonacci(n):
    if n <= 0:
        return n
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


# Exemplo de uso da função para calcular o número Fibonacci para n = 10
resultado = fibonacci(10)
print(f"O número Fibonacci correspondente é: {resultado}")

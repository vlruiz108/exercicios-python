n = 0


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


resultado = fibonacci(10)
print(f'O numero fibonacci {resultado}')
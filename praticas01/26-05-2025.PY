def fibonacci(n):
    sequencia = []
    a, b = 0, 1

    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b  # Atualize os valores dentro do loop

    return sequencia


n = int(input("Digite quantos números da sequência de Fibonacci você quer: "))
resultado = fibonacci(n)
print(f"Sequência de Fibonacci: {resultado}")
50

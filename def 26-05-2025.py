def subtrair(x, y):
    return x-y


def dividir(x, y):
    return x / y


def ao_quadrado_da_soma(x, y):
    return (x + y) ** 2


def subtrair(x, y):
    return x - y


def executar_operacao(funcao, x, y):
    return funcao(x, y)


x = 5
y = 2

print(executar_operacao(subtrair, x, y))
print(executar_operacao(dividir, x, y))
print(executar_operacao(ao_quadrado_da_soma, x, y))

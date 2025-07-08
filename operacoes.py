import math  # Biblioteca para funções matemáticas

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: número negativo não tem raiz real."
    return math.sqrt(a)

def porcentagem(a, b):
    # Retorna o valor que é b% de a
    return (a * b) / 100

def potencia(base, expoente):
    return base ** expoente

def modulo(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a % b

from operacoes import somar, subtrair, multiplicar, dividir, raiz_quadrada, porcentagem, potencia, modulo
from historico import salvar_historico, mostrar_historico, limpar_historico


def mostrar_menu():
    print("Calculadora Simples")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada")
    print("6 - Porcentagem")
    print("7 - Potência")
    print("8 - Módulo (resto da divisão)")
    print("9 - Ver histórico")
    print("10 - Limpar histórico")


def executar_calculo():
    mostrar_menu()
    opcao = input("Escolha a operação (1-9): ")

    if opcao == '1':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = somar(num1, num2)
        print("Resultado:", resultado)
        salvar_historico(f"{num1} + {num2}", resultado)

    elif opcao == '2':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = subtrair(num1, num2)
        print("Resultado:", resultado)
        salvar_historico(f"{num1} - {num2}", resultado)

    elif opcao == '3':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = multiplicar(num1, num2)
        print("Resultado:", resultado)
        salvar_historico(f"{num1} * {num2}", resultado)

    elif opcao == '4':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = dividir(num1, num2)
        print("Resultado:", resultado)
        salvar_historico(f"{num1} / {num2}", resultado)

    elif opcao == '5':
        num = float(input("Digite o número para calcular a raiz quadrada: "))
        resultado = raiz_quadrada(num)
        print("Resultado:", resultado)
        salvar_historico(f"√{num}", resultado)

    elif opcao == '6':
        num1 = float(input("Digite o valor base: "))
        num2 = float(input("Digite a porcentagem (%): "))
        resultado = porcentagem(num1, num2)
        print("Resultado:", resultado)
        salvar_historico(f"{num2}% de {num1}", resultado)

    elif opcao == '7':
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        resultado = potencia(base, expoente)
        print("Resultado:", resultado)
        salvar_historico(f"{base} ^ {expoente}", resultado)

    elif opcao == '8':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = modulo(num1, num2)
        print("Resultado:", resultado)
        salvar_historico(f"{num1} % {num2}", resultado)

    elif opcao == '9':
        print("Histórico:")
        print(mostrar_historico())

    elif opcao == '10':
        limpar_historico()
        print("Histórico apagado com sucesso.")

    else:
        print("Opção inválida.")



if __name__ == "__main__":
    executar_calculo()

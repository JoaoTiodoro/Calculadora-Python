from operacoes import somar, subtrair, multiplicar, dividir

def mostrar_menu():
    print("Calculadora Simples")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

def executar_calculo():
    mostrar_menu()
    opcao = input("Digite a opção (1/2/3/4): ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: você deve digitar números.")
        return

    if opcao == '1':
        print("Resultado:", somar(num1, num2))
    elif opcao == '2':
        print("Resultado:", subtrair(num1, num2))
    elif opcao == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif opcao == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    executar_calculo()

import tkinter as tk
from operacoes import somar, subtrair, multiplicar, dividir, raiz_quadrada, porcentagem, potencia, modulo

# Janela principal
janela = tk.Tk()
janela.title("Calculadora João Tiodoro")
janela.geometry("360x570")
janela.configure(bg="#f4f4f4")
janela.resizable(False, False)

# Estilo visual
fonte = ("Segoe UI", 12)
cor_botao = "#3498db"
cor_texto = "#ffffff"

# Container principal
container = tk.Frame(janela, bg="#f4f4f4")
container.pack(pady=10)

# Labels e campos de entrada
label1 = tk.Label(container, text="Digite o primeiro número:", font=fonte, bg="#f4f4f4")
label1.pack()
entrada1 = tk.Entry(container, font=fonte, width=25, justify="center")
entrada1.pack(pady=5)

label2 = tk.Label(container, text="Digite o segundo número:", font=fonte, bg="#f4f4f4")
label2.pack()
entrada2 = tk.Entry(container, font=fonte, width=25, justify="center")
entrada2.pack(pady=5)

# Label de resultado
resultado_label = tk.Label(container, text="Resultado:", font=("Segoe UI", 14, "bold"), bg="#f4f4f4", fg="#333")
resultado_label.pack(pady=12)

# Função de cálculo genérica
def calcular(funcao, usar_segundo=True):
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get()) if usar_segundo else None
        resultado = funcao(num1, num2) if usar_segundo else funcao(num1)
        resultado_label.config(text=f"Resultado: {resultado}")
    except Exception as e:
        resultado_label.config(text=f"Erro: {str(e)}")

# Função para criar botões estilizados
def criar_botao(texto, comando):
    return tk.Button(
        container,
        text=texto,
        command=comando,
        font=fonte,
        width=35,
        bg=cor_botao,
        fg=cor_texto,
        activebackground="#2980b9",
        relief="raised",
        bd=2
    )

# Botões de operação com textos claros
criar_botao("Somar (1º + 2º)", lambda: calcular(somar)).pack(pady=3)
criar_botao("Subtrair (1º - 2º)", lambda: calcular(subtrair)).pack(pady=3)
criar_botao("Multiplicar (1º × 2º)", lambda: calcular(multiplicar)).pack(pady=3)
criar_botao("Dividir (1º ÷ 2º)", lambda: calcular(dividir)).pack(pady=3)
criar_botao("Raiz quadrada (somente do 1º)", lambda: calcular(raiz_quadrada, usar_segundo=False)).pack(pady=3)
criar_botao("Porcentagem (quanto é 2º % de 1º)", lambda: calcular(porcentagem)).pack(pady=3)
criar_botao("Potência (1º elevado ao 2º)", lambda: calcular(potencia)).pack(pady=3)
criar_botao("Módulo (resto de 1º ÷ 2º)", lambda: calcular(modulo)).pack(pady=3)

# Inicia a interface gráfica
janela.mainloop()

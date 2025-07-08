def salvar_historico(operacao, resultado):
    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{operacao} = {resultado}\n")

def mostrar_historico():
    try:
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            return conteudo if conteudo else "Histórico vazio."
    except FileNotFoundError:
        return "Nenhum histórico encontrado."

def limpar_historico():
    with open("historico.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("")  # Escreve nada = apaga tudo

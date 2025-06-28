from model.aluno import Aluno


def solicitar_dados_aluno():
    print("=== Cadastro de Aluno ===")
    nome = input("Nome do aluno: ").strip()
    email = input("Email do aluno: ").strip()
    return nome, email


def mostrar_mensagem_sucesso(aluno: Aluno):
    print(f"Aluno '{aluno.nome}' cadastrado com sucesso! (ID: {aluno.id})\n")

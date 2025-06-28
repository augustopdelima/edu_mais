from model.professor import Professor


def solicitar_dados_professor():
    print("=== Cadastro de Professor ===")
    nome = input("Nome do professor: ").strip()
    email = input("Email do professor: ").strip()
    return nome, email


def mostrar_mensagem_sucesso(professor: Professor):
    print(
        f"Professor '{professor.nome}' cadastrado com sucesso! (ID: {professor.id})\n")

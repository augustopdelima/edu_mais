from model.disciplina import Disciplina


def solicitar_dados_disciplina():
    print("=== Cadastro de Disciplina ===")
    nome = input("Nome da disciplina: ").strip()
    descricao = input("Descrição: ").strip()
    semestre = input("Semestre: ").strip()
    return nome, descricao, semestre


def mostrar_mensagem_sucesso(disciplina: Disciplina):
    print(
        f"Disciplina '{disciplina.nome}' cadastrada com sucesso! (ID: {disciplina.id})\n")

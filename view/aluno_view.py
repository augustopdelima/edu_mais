from typing import List
from model.aluno import Aluno


def exibir_aluno(aluno: Aluno) -> None:
    print("=== Detalhes do Aluno ===")
    print(f"ID: {aluno.id}")
    print(f"Nome: {aluno.nome}")
    print(f"Email: {aluno.email}")
    print(f"Matrícula: {aluno.matricula}")
    print("=========================\n")


def listar_alunos(alunos: List[Aluno]) -> None:
    print("=== Lista de Alunos ===")
    for aluno in alunos:
        print(f"[{aluno.id}] {aluno.nome} - {aluno.email} - {aluno.matricula}")
    print("======================\n")


def exibir_aluno_nao_encontrado(id: int) -> None:
    print(f"Aluno com ID {id} não encontrado.\n")


def mostrar_mensagem_sucesso(mensagem: str) -> None:
    print(f"Sucesso: {mensagem}\n")


def mostrar_mensagem_erro(mensagem: str) -> None:
    print(f"Erro: {mensagem}\n")

from model.aluno import Aluno
from typing import List


def exibir_aluno(aluno: Aluno):
    print("=== Professor ===")
    print(f"ID: {aluno.id}")
    print(f"Nome: {aluno.nome}")
    print(f"Email: {aluno.email}")
    print("=================\n")


def listar_alunos(alunos: List[Aluno]):
    print("=== Lista de Professores ===")
    for aluno in alunos:
        print(f"[{aluno.id}] {aluno.nome} <{aluno.email}>")
    print("=============================\n")


def exibir_aluno_nao_encontrado(id: int):
    print(f"Aluno com ID {id} não encontrado.\n")

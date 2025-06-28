from model.professor import Professor
from typing import List


def exibir_professor(professor: Professor) -> None:
    print("=== Professor ===")
    print(f"ID: {professor.id}")
    print(f"Nome: {professor.nome}")
    print(f"Email: {professor.email}")
    print("=================\n")


def listar_professores(professores: List[Professor]) -> None:
    print("=== Lista de Professores ===")
    for prof in professores:
        print(f"[{prof.id}] {prof.nome} <{prof.email}>")
    print("=============================\n")


def exibir_professor_nao_encontrado(id: int) -> None:
    print(f"Professor com ID {id} não encontrado.\n")

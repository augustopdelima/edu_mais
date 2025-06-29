# view/professor_view.py
from typing import List
from model.professor import Professor


def exibir_professor(professor: Professor) -> None:
    print("=== Detalhes do Professor ===")
    print(f"ID: {professor.id}")
    print(f"Nome: {professor.nome}")
    print(f"Email: {professor.email}")
    print("=============================\n")


def listar_professores(professores: List[Professor]) -> None:
    print("=== Lista de Professores ===")
    for p in professores:
        print(f"[{p.id}] {p.nome} <{p.email}>")
    print("============================\n")


def exibir_professor_nao_encontrado(id: int) -> None:
    print(f"Professor com ID {id} não encontrado.\n")


def mostrar_mensagem_sucesso(mensagem: str) -> None:
    print(f"Sucesso: {mensagem}\n")


def mostrar_mensagem_erro(mensagem: str) -> None:
    print(f"Erro: {mensagem}\n")

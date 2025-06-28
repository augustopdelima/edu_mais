from typing import List
from model.disciplina import Disciplina


def exibir_disciplina(disciplina: Disciplina) -> None:
    print("=== Detalhes da Disciplina ===")
    print(f"ID: {disciplina.id}")
    print(f"Nome: {disciplina.nome}")
    print(f"Semestre: {disciplina.semestre}")
    print(f"Descrição: {disciplina.descricao}")
    print(
        f"Professor: {disciplina.professor.nome} ({disciplina.professor.email})")
    print("==============================\n")


def listar_disciplinas(disciplinas: List[Disciplina]) -> None:
    print("=== Lista de Disciplinas ===")
    for d in disciplinas:
        print(f"[{d.id}] {d.nome} - {d.semestre} - Prof: {d.professor.nome}")
    print("============================\n")


def exibir_disciplina_nao_encontrada(id: int) -> None:
    print(f"Disciplina com ID {id} não encontrada.\n")


def mostrar_mensagem_sucesso(mensagem: str) -> None:
    print(f"Sucesso: {mensagem}\n")


def mostrar_mensagem_erro(mensagem: str) -> None:
    print(f"Erro: {mensagem}\n")

from model.turma import Turma
from typing import List


def exibir_turma(turma: Turma) -> None:
    print("=== Turma ===")
    print(f"ID: {turma.id}")
    print(f"Nome: {turma.nome}")
    print(f"Ano: {turma.ano}")
    print(f"Semestre: {turma.semestre}")
    print(f"Disciplina: {turma.disciplina}")
    print("=================\n")


def listar_turmas(turmas: List[Turma]) -> None:
    print("=== Lista de Turmas ===")
    for turma in turmas:
        print(
            f"[{turma.id}] {turma.nome} - {turma.disciplina} ({turma.ano}/{turma.semestre})")
    print("========================\n")


def exibir_turma_nao_encontrada(id: int) -> None:
    print(f"Turma com ID {id} não encontrada.\n")


def solicitar_dados_turma():
    print("=== Cadastro de Turma ===")
    nome = input("Nome da turma: ").strip()
    ano = int(input("Ano da turma (ex: 2025): ").strip())
    semestre = int(input("Semestre da turma (ex: 1 ou 2): ").strip())
    disciplina = input("Disciplina associada: ").strip()
    return nome, ano, semestre, disciplina


def mostrar_mensagem_sucesso(turma):
    print(f"Turma '{turma.nome}' cadastrada com sucesso! (ID: {turma.id})\n")

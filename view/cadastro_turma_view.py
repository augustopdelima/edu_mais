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
            print(f"[{turma.id}] {turma.nome} - {turma.disciplina} ({turma.ano}/{turma.semestre})")
        print("========================\n")

    def exibir_turma_nao_encontrada(id: int) -> None:
        print(f"Turma com ID {id} não encontrada.\n")
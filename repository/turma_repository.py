from typing import List, Optional
from model.turma import Turma


class TurmaRepository:
    def __init__(self):
        self.turmas: List[Turma] = []

    def salvar(self, turma: Turma) -> None:
        print(f"[Repositório] Salvando turma ID {turma.id}")
        self.turmas.append(turma)

    def listar_todos(self) -> List[Turma]:
        print("[Repositório] Listando todas as turmas")
        return self.turmas

    def buscar_por_id(self, id: int) -> Optional[Turma]:
        print(f"[Repositório] Buscando turma pelo ID {id}")
        for turma in self.turmas:
            if turma.id == id:
                return turma
        return None

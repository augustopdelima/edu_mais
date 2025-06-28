from model.turma import Turma
from typing import List, Optional


class TurmaRepository:
    def __init__(self) -> None:
        self.turmas: List[Turma] = []

    def salvar(self, turma: Turma) -> None:
        self.turmas.append(turma)

    def listar_todos(self) -> List[Turma]:
        return self.turmas

    def buscar_por_id(self, id: int) -> Optional[Turma]:
        for turma in self.turmas:
            if turma.id == id:
                return turma
        return None
from model.disciplina import Disciplina
from typing import List, Optional


class DisciplinaRepository:
    def __init__(self) -> None:
        self.disciplinas: List[Disciplina] = []

    def salvar(self, aluno: Disciplina) -> None:
        self.disciplinas.append(aluno)

    def listar_todos(self) -> List[Disciplina]:
        return self.disciplinas

    def buscar_por_id(self, id: int) -> Optional[Disciplina]:
        for disciplina in self.disciplinas:
            if disciplina.id == id:
                return disciplina
        return None

from model.professor import Professor
from typing import List, Optional


class ProfessorRepository:
    def __init__(self) -> None:
        self.professores: List[Professor] = []

    def salvar(self, professor: Professor) -> None:
        self.professores.append(professor)

    def listar_todos(self) -> List[Professor]:
        return self.professores

    def buscar_por_id(self, id: int) -> Optional[Professor]:
        for professor in self.professores:
            if professor.id == id:
                return professor
        return None

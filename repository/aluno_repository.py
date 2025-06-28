from model.aluno import Aluno
from typing import List, Optional


class AlunoRepository:
    def __init__(self) -> None:
        self.alunos: List[Aluno] = []

    def salvar(self, aluno: Aluno) -> None:
        self.alunos.append(aluno)

    def listar_todos(self) -> List[Aluno]:
        return self.alunos

    def buscar_por_id(self, id: int) -> Optional[Aluno]:
        for alunos in self.alunos:
            if alunos.id == id:
                return alunos
        return None

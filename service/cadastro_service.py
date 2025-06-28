from model.professor import Professor
from repository.professor_repository import ProfessorRepository
from typing import List, Optional


class CadastroService:
    def __init__(self) -> None:
        self.professor_repository = ProfessorRepository()

    def cadastrar_professor(self, nome: str, email: str) -> Professor:
        novo_id: int = len(self.professor_repository.listar_todos()) + 1
        professor = Professor(id=novo_id, nome=nome, email=email)
        self.professor_repository.salvar(professor)
        return professor

    def listar_professores(self) -> List[Professor]:
        return self.professor_repository.listar_todos()

    def buscar_professor_por_id(self, id: int) -> Optional[Professor]:
        return self.professor_repository.buscar_por_id(id)

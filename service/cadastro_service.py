from model.professor import Professor
from repository.professor_repository import ProfessorRepository


class CadastroService:
    def __init__(self):
        self.professor_repository = ProfessorRepository()

    def cadastrar_professor(self, nome: str, email: str):
        novo_id: int = len(self.professor_repository.listar_todos()) + 1
        professor = Professor(id=novo_id, nome=nome, email=email)
        self.professor_repository.salvar(professor)
        return professor

    def listar_professores(self):
        return self.professor_repository.listar_todos()

    def buscar_professor_por_id(self, id: int):
        return self.professor_repository.buscar_por_id(id)

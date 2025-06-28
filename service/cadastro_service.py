from model.professor import Professor
from model.aluno import Aluno
from repository.professor_repository import ProfessorRepository
from repository.aluno_repository import AlunoRepository


class CadastroService:
    def __init__(self):
        self.professor_repository = ProfessorRepository()
        self.aluno_repository = AlunoRepository()

    def cadastrar_professor(self, nome: str, email: str):
        novo_id: int = len(self.professor_repository.listar_todos()) + 1
        professor = Professor(id=novo_id, nome=nome, email=email)
        self.professor_repository.salvar(professor)
        return professor

    def cadastrar_aluno(self, nome: str, email: str):
        novo_id: int = len(self.aluno_repository.listar_todos()) + 1
        aluno = Aluno(id=novo_id, nome=nome, email=email)
        self.aluno_repository.salvar(aluno)
        return aluno

from model.professor import Professor
from model.aluno import Aluno
from model.disciplina import Disciplina
from repository.professor_repository import ProfessorRepository
from repository.aluno_repository import AlunoRepository
from repository.disciplina_repository import DisciplinaRepository


class CadastroService:
    def __init__(
        self,
        aluno_repository: AlunoRepository = None,
        professor_repository: ProfessorRepository = None,
        disciplina_repository: DisciplinaRepository = None
    ):
        self.aluno_repository = aluno_repository or AlunoRepository()
        self.professor_repository = professor_repository or ProfessorRepository()
        self.disciplinas = disciplina_repository or DisciplinaRepository()

    def cadastrar_professor(self, nome: str, email: str):
        novo_id = len(self.professor_repository.listar_todos()) + 1
        professor = Professor(id=novo_id, nome=nome, email=email)
        self.professor_repository.salvar(professor)
        return professor

    def cadastrar_aluno(self, nome: str, email: str):
        novo_id = len(self.aluno_repository.listar_todos()) + 1
        aluno = Aluno(id=novo_id, nome=nome, email=email)
        self.aluno_repository.salvar(aluno)
        return aluno

    def cadastrar_disciplina(self, nome: str, descricao: str, semestre: str):
        novo_id = len(self.disciplinas) + 1
        disciplina = Disciplina(id=novo_id, nome=nome,
                                descricao=descricao, semestre=semestre)
        self.disciplinas.append(disciplina)
        return disciplina

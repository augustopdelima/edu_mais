from service.cadastro_service import CadastroService
from view.aluno_view import exibir_aluno, listar_alunos, exibir_aluno_nao_encontrado
from repository.aluno_repository import AlunoRepository


class AlunoController:
    def __init__(self):
        self.cadastro_service = CadastroService()
        self.aluno_repository = AlunoRepository()

    def cadastrar_aluno(self, nome: str, email: str):
        aluno = self.cadastro_service.cadastrar_aluno(nome, email)
        exibir_aluno(aluno)

    def listar_aluno(self):
        alunos = self.aluno_repository.listar_todos()
        listar_alunos(alunos)

    def mostrar_aluno_por_id(self, id: int):
        aluno = self.aluno_repository.buscar_por_id(id)
        if aluno:
            exibir_aluno(aluno)
        else:
            exibir_aluno_nao_encontrado(id)

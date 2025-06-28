from service.cadastro_service import CadastroService
from view.aluno_view import exibir_aluno, listar_alunos, exibir_aluno_nao_encontrado
from view.cadastro_aluno_view import mostrar_mensagem_sucesso, solicitar_dados_aluno
from repository.aluno_repository import AlunoRepository


class AlunoController:
    def __init__(self):
        self.aluno_repository = AlunoRepository()
        self.cadastro_service = CadastroService(
            aluno_repository=self.aluno_repository)

    def cadastrar_aluno(self):
        nome, email = solicitar_dados_aluno()
        aluno = self.cadastro_service.cadastrar_aluno(nome, email)
        mostrar_mensagem_sucesso(aluno=aluno)

    def listar_aluno(self):
        alunos = self.aluno_repository.listar_todos()
        listar_alunos(alunos)

    def mostrar_aluno_por_id(self, id: int):
        aluno = self.aluno_repository.buscar_por_id(id)
        if aluno:
            exibir_aluno(aluno)
        else:
            exibir_aluno_nao_encontrado(id)

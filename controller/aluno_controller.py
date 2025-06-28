from service.cadastro_service import CadastroService
from view.aluno_view import exibir_aluno, listar_alunos, exibir_aluo_nao_encontrado


class AlunoController:
    def __init__(self):
        self.cadastro_service = CadastroService()

    def cadastrar_aluno(self, nome: str, email: str):
        aluno = self.cadastro_service.cadastrar_aluno(nome, email)
        exibir_aluno(aluno)

    def listar_aluno(self):
        professores = self.cadastro_service.listar_alunos()
        listar_alunos(professores)

    def mostrar_aluno_por_id(self, id: int):
        aluno = self.cadastro_service.buscar_aluno_por_id(id)
        if aluno:
            exibir_aluno(aluno)
        else:
            exibir_aluo_nao_encontrado(id)

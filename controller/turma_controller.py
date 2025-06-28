from service.cadastro_service import CadastroService
from repository.turma_repository import TurmaRepository
from view.cadastro_turma_view import exibir_turma, listar_turmas, exibir_turma_nao_encontrada, mostrar_mensagem_sucesso, solicitar_dados_turma


class TurmaController:
    def __init__(self):
        self.turma_repository = TurmaRepository()
        self.cadastro_service = CadastroService(
            turma_repository=self.turma_repository)

    def cadastrar_turma_interativo(self):
        nome, ano, semestre, disciplina = solicitar_dados_turma()
        turma = self.cadastro_service.cadastrar_turma(
            nome, ano, semestre, disciplina)
        mostrar_mensagem_sucesso(turma)

    def listar_turmas(self):
        turmas = self.cadastro_service.listar_turmas()
        listar_turmas(turmas)

    def buscar_turma_por_id(self, id: int):
        turma = self.cadastro_service.buscar_turma_por_id(id)
        if turma:
            exibir_turma(turma)
        else:
            exibir_turma_nao_encontrada(id)

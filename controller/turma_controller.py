from service.cadastro_service import CadastroService
from view.cadastro_turma_view import exibir_turma, listar_turmas, exibir_turma_nao_encontrada

class TurmaController:
    def __init__(self):
        self.cadastro_service = CadastroService()

    def cadastrar_turma(self, nome: str, ano: int, semestre: int, disciplina: str):
        turma = self.cadastro_service.cadastrar_turma(nome, ano, semestre, disciplina)
        exibir_turma(turma)

    def listar_turmas(self):
        turmas = self.cadastro_service.listar_turmas()
        listar_turmas(turmas)

    def buscar_turma_por_id(self, id: int):
        turma = self.cadastro_service.buscar_turma_por_id(id)
        if turma:
            exibir_turma(turma)
        else:
            exibir_turma_nao_encontrada(id)
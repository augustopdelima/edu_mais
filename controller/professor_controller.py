from repository.professor_repository import ProfessorRepository
from service.cadastro_service import CadastroService
from view.professor_view import exibir_professor, listar_professores, exibir_professor_nao_encontrado
from view.cadastro_professor_view import mostrar_mensagem_sucesso, solicitar_dados_professor


class ProfessorController:
    def __init__(self) -> None:
        self.professor_repository = ProfessorRepository()
        self.cadastro_service = CadastroService(
            professor_repository=self.professor_repository)

    def cadastrar_professor(self):
        nome, email = solicitar_dados_professor()
        professor = self.cadastro_service.cadastrar_professor(nome, email)
        mostrar_mensagem_sucesso(professor)

    def listar_professores(self) -> None:
        professores = self.professor_repository.listar_todos()
        listar_professores(professores)

    def mostrar_professor_por_id(self, id: int) -> None:
        professor = self.professor_repository.buscar_por_id(id)
        if professor:
            exibir_professor(professor)
        else:
            exibir_professor_nao_encontrado(id)

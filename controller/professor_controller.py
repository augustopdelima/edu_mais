from service.cadastro_service import CadastroService
from view.professor_view import exibir_professor, listar_professores, exibir_professor_nao_encontrado
from repository.professor_repository import ProfessorRepository


class ProfessorController:
    def __init__(self) -> None:
        self.cadastro_service = CadastroService()
        self.professor_repository = ProfessorRepository()

    def cadastrar_professor(self, nome: str, email: str) -> None:
        professor = self.cadastro_service.cadastrar_professor(nome, email)
        exibir_professor(professor)

    def listar_professores(self) -> None:
        professores = self.professor_repository.listar_todos()
        listar_professores(professores)

    def mostrar_professor_por_id(self, id: int) -> None:
        professor = self.professor_repository.buscar_por_id(id)
        if professor:
            exibir_professor(professor)
        else:
            exibir_professor_nao_encontrado(id)

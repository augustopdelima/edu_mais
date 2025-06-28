from service.cadastro_service import CadastroService
from view.cadastro_disciplina_view import solicitar_dados_disciplina, mostrar_mensagem_sucesso
from repository.disciplina_repository import DisciplinaRepository


class DisciplinaController:
    def __init__(self):
        self.disciplina_repository = DisciplinaRepository()
        self.cadastro_service = CadastroService(
            disciplina_repository=self.disicplina_repository)

    def cadastrar_disciplina(self):
        nome, descricao, semestre = solicitar_dados_disciplina()
        disciplina = self.cadastro_service.cadastrar_disciplina(
            nome, descricao, semestre)
        mostrar_mensagem_sucesso(disciplina)

    def listar_disciplinas(self):
        disciplinas = self.disciplina_repository.listar_todos()
        print(disciplinas)

    def mostrar_disciplina_por_id(self, id: int):
        disciplina = self.disciplina_repository.buscar_por_id(id)
        if disciplina:
            print(disciplina)
        else:
            print("Não encontrado", id)

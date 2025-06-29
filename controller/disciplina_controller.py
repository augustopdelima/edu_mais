from model.professor import Professor
from service.disciplina_service import DisciplinaService
from view.disciplina_view import (
    exibir_disciplina,
    listar_disciplinas,
    exibir_disciplina_nao_encontrada,
    mostrar_mensagem_sucesso,
)


class DisciplinaController:
    def __init__(self, disciplina_service: DisciplinaService):
        print("[Controlador] Inicializando DisciplinaController")
        self.disciplina_service = disciplina_service

    def cadastrar_disciplina(self, nome: str, semestre: str, descricao: str, professor: Professor) -> None:
        print(f"[Controlador] Cadastrando disciplina: {nome}")
        disciplina = self.disciplina_service.cadastrar_disciplina(
            nome, semestre, descricao, professor)
        mostrar_mensagem_sucesso(
            f"Disciplina '{disciplina.nome}' cadastrada com sucesso!")

    def listar_disciplinas(self) -> None:
        print("[Controlador] Listando disciplinas")
        disciplinas = self.disciplina_service.listar_disciplinas()
        listar_disciplinas(disciplinas)

    def mostrar_disciplina_por_id(self, id: int) -> None:
        print(f"[Controlador] Mostrando disciplina ID {id}")
        disciplina = self.disciplina_service.buscar_disciplina_por_id(id)
        if disciplina:
            exibir_disciplina(disciplina)
        else:
            exibir_disciplina_nao_encontrada(id)

    def deletar_disciplina(self, id: int) -> None:
        print(f"[Controlador] Deletando disciplina ID {id}")
        self.disciplina_service.remover_disciplina(id)
        mostrar_mensagem_sucesso(f"Disciplina ID {id} removida com sucesso!")

from model.usuario import Usuario
from security.permissao import Permissao
from security.validador_permissao import validar_permissao
from service.professor_service import ProfessorService
from view.professor_view import (
    exibir_professor,
    listar_professores,
    exibir_professor_nao_encontrado,
    mostrar_mensagem_sucesso,
)


class ProfessorController:
    def __init__(self, professor_service: ProfessorService):
        print("[Controlador] Inicializando ProfessorController")
        self.professor_service = professor_service

    def cadastrar_professor(self, usuario: Usuario, nome: str, email: str, senha: str) -> None:

        validar_permissao(usuario, [Permissao.COORDENADOR])

        print(f"[Controlador] Cadastrando professor: {nome}")
        professor = self.professor_service.cadastrar_professor(
            nome, email, senha)
        mostrar_mensagem_sucesso(
            f"Professor '{professor.nome}' cadastrado com sucesso!")

    def listar_professores(self) -> None:
        print("[Controlador] Listando professores")
        professores = self.professor_service.listar_professores()
        listar_professores(professores)

    def mostrar_professor_por_id(self, id: int) -> None:
        print(f"[Controlador] Mostrando professor ID {id}")
        professor = self.professor_service.buscar_professor_por_id(id)
        if professor:
            exibir_professor(professor)
        else:
            exibir_professor_nao_encontrado(id)

    def deletar_professor(self, usuario: Usuario, id: int) -> None:

        validar_permissao(usuario, [Permissao.COORDENADOR])

        print(f"[Controlador] Deletando professor ID {id}")
        self.professor_service.remover_professor(id)
        mostrar_mensagem_sucesso(f"Professor ID {id} removido com sucesso!")

from model.usuario import Usuario
from security.permissao import Permissao
from security.validador_permissao import validar_permissao
from service.turma_service import TurmaService
from view.turma_view import (
    exibir_turma,
    listar_turmas,
    exibir_turma_nao_encontrada,
    mostrar_mensagem_sucesso
)

from model.disciplina import Disciplina


class TurmaController:
    def __init__(self, turma_service: TurmaService):
        print("[Controlador] Inicializando TurmaController")
        self.turma_service = turma_service

    def cadastrar_turma(self, usuario: Usuario, nome: str, ano: int, semestre: int, disciplina: Disciplina, alunos: list = None) -> None:

        validar_permissao(usuario, [Permissao.COORDENADOR])

        print("[Controlador] Cadastrando turma")
        turma = self.turma_service.cadastrar_turma(
            nome, ano, semestre, disciplina, alunos)
        mostrar_mensagem_sucesso(
            f"Turma '{turma.nome}' cadastrada com sucesso! (ID: {turma.id})")

    def listar_turmas(self) -> None:
        print("[Controlador] Listando turmas")
        turmas = self.turma_service.listar_turmas()
        listar_turmas(turmas)

    def mostrar_turma_por_id(self, id: int) -> None:
        print(f"[Controlador] Mostrando turma ID {id}")
        turma = self.turma_service.buscar_turma_por_id(id)
        if turma:
            exibir_turma(turma)
        else:
            exibir_turma_nao_encontrada(id)

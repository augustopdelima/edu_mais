# controller/aluno_controller.py
from typing import Optional
from model.aluno import Aluno
from service.aluno_service import AlunoService
from view.aluno_view import exibir_aluno, listar_alunos, exibir_aluno_nao_encontrado, mostrar_mensagem_sucesso, mostrar_mensagem_erro


class AlunoController:
    def __init__(self, aluno_service: AlunoService):
        self.aluno_service = aluno_service

    def cadastrar_aluno(self, nome: str, email: str, matricula: str) -> None:
        print(f"Controlador: cadastrar aluno {nome}")
        aluno = self.aluno_service.cadastrar_aluno(nome, email, matricula)
        mostrar_mensagem_sucesso(f"Aluno {aluno.nome} cadastrado com sucesso!")

    def atualizar_aluno(self, id: int, nome: str, email: str, matricula: str) -> None:
        print(f"Controlador: atualizar aluno ID {id}")
        aluno = self.aluno_service.atualizar_aluno(id, nome, email, matricula)
        if aluno:
            mostrar_mensagem_sucesso(f"Aluno ID {id} atualizado com sucesso!")
        else:
            mostrar_mensagem_erro(
                f"Aluno ID {id} não encontrado para atualização.")

    def listar_alunos(self) -> None:
        print("Controlador: listar alunos")
        alunos = self.aluno_service.listar_alunos()
        listar_alunos(alunos)

    def mostrar_aluno_por_id(self, id: int) -> None:
        print(f"Controlador: mostrar aluno ID {id}")
        aluno = self.aluno_service.buscar_aluno_por_id(id)
        if aluno:
            exibir_aluno(aluno)
        else:
            exibir_aluno_nao_encontrado(id)

    def deletar_aluno(self, id: int) -> None:
        print(f"Controlador: deletar aluno ID {id}")
        self.aluno_service.remover_aluno(id)
        mostrar_mensagem_sucesso(f"Aluno ID {id} removido com sucesso!")

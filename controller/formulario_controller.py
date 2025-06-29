
from typing import List

from model.disciplina import Disciplina
from model.turma import Turma
from model.coordenador import Coordenador
from model.professor import Professor
from model.questao import Questao
from service.formulario_service import FormularioService
from view.formulario_view import (
    exibir_formulario,
    listar_formularios,
    exibir_formulario_nao_encontrado,
    mostrar_mensagem_sucesso,
)


class FormularioController:
    def __init__(self, formulario_service: FormularioService):
        print("[Controlador] Inicializando FormularioController")
        self.formulario_service = formulario_service

    def cadastrar_formulario(self, data_aplicacao: str, disciplina: Disciplina,
                             turma: Turma, criado_por: Coordenador,
                             avaliar: Professor, perguntas: List[Questao]) -> None:
        print("[Controlador] Cadastrando formulário")
        formulario = self.formulario_service.cadastrar_formulario(
            data_aplicacao, disciplina, turma, criado_por, avaliar, perguntas
        )
        mostrar_mensagem_sucesso(
            f"Formulário ID {formulario.id} cadastrado com sucesso!")

    def listar_formularios(self) -> None:
        print("[Controlador] Listando formulários")
        formularios = self.formulario_service.listar_formularios()
        listar_formularios(formularios)

    def mostrar_formulario_por_id(self, id: int) -> None:
        print(f"[Controlador] Mostrando formulário ID {id}")
        formulario = self.formulario_service.buscar_formulario_por_id(id)
        if formulario:
            exibir_formulario(formulario)
        else:
            exibir_formulario_nao_encontrado(id)

    def deletar_formulario(self, id: int) -> None:
        print(f"[Controlador] Deletando formulário ID {id}")
        self.formulario_service.remover_formulario(id)
        mostrar_mensagem_sucesso(f"Formulário ID {id} removido com sucesso!")

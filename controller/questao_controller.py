# controller/questao_controller.py
from typing import Optional
from model.questao import Questao
from service.questao_service import QuestaoService
from view.questao_view import (
    exibir_questao,
    listar_questoes,
    exibir_questao_nao_encontrada,
    mostrar_mensagem_sucesso,
    mostrar_mensagem_erro,
)


class QuestaoController:
    def __init__(self, questao_service: QuestaoService):
        print("[Controlador] Inicializando QuestaoController")
        self.questao_service = questao_service

    def cadastrar_questao(self, tipo: str, pergunta: str) -> None:
        print(f"[Controlador] Cadastrando questão: {pergunta}")
        questao = self.questao_service.cadastrar_questao(tipo, pergunta)
        mostrar_mensagem_sucesso(
            f"Questão '{questao.pergunta}' cadastrada com sucesso!")

    def listar_questoes(self) -> None:
        print("[Controlador] Listando questões")
        questoes = self.questao_service.listar_questoes()
        listar_questoes(questoes)

    def mostrar_questao_por_id(self, id: int) -> None:
        print(f"[Controlador] Mostrando questão ID {id}")
        questao = self.questao_service.buscar_questao_por_id(id)
        if questao:
            exibir_questao(questao)
        else:
            exibir_questao_nao_encontrada(id)

    def deletar_questao(self, id: int) -> None:
        print(f"[Controlador] Deletando questão ID {id}")
        self.questao_service.remover_questao(id)
        mostrar_mensagem_sucesso(f"Questão ID {id} removida com sucesso!")

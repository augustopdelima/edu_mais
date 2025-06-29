
from typing import List, Optional
from model.questao import Questao
from repository.questao_repository import QuestaoRepository


class QuestaoService:
    def __init__(self, questao_repository: QuestaoRepository):
        print("[Serviço] Inicializando QuestaoService")
        self.questao_repository = questao_repository

    def cadastrar_questao(self, tipo: str, pergunta: str) -> Questao:
        print(f"[Serviço] Cadastrando questão: {pergunta}")
        return Questao(1, tipo, pergunta)

    def listar_questoes(self) -> List[Questao]:
        print("[Serviço] Listando questões")
        return []

    def buscar_questao_por_id(self, id: int) -> Optional[Questao]:
        print(f"[Serviço] Buscando questão por ID: {id}")
        return None

    def remover_questao(self, id: int) -> None:
        print(f"[Serviço] Removendo questão com ID: {id}")

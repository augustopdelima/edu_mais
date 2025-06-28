from typing import List, Optional
from model.questao import Questao


class QuestaoRepository:

    def __init__(self):
        self.questoes = list[Questao]

    def salvar(self, questao: Questao) -> None:
        print(f"[Repositório] Salvando questão: {questao.pergunta}")

    def listar_todas(self) -> List[Questao]:
        print("[Repositório] Listando todas as questões")
        return []

    def buscar_por_id(self, id: int) -> Optional[Questao]:
        print(f"[Repositório] Buscando questão pelo ID: {id}")
        return None

    def deletar(self, id: int) -> None:
        print(f"[Repositório] Deletando questão com ID: {id}")

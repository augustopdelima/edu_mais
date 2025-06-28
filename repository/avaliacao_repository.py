from typing import List, Optional
from model.avaliacao import Avaliacao


class AvaliacaoRepository:
    def __init__(self):
        self.avaliacoes: List[Avaliacao] = []

    def salvar(self, avaliacao: Avaliacao) -> None:
        self.avaliacoes.append(avaliacao)

    def listar_todos(self) -> List[Avaliacao]:
        return self.avaliacoes

    def buscar_por_id(self, id: int) -> Optional[Avaliacao]:
        for avaliacao in self.avaliacoes:
            if avaliacao.id == id:
                return avaliacao
        return None

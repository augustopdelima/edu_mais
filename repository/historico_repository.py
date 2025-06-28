from model.historico import HistoricoAvaliacao
from typing import List, Optional


class HistoricoAvaliacaoRepository:
    def __init__(self):
        self.historicos: List[HistoricoAvaliacao] = []

    def salvar(self, historico: HistoricoAvaliacao) -> None:
        self.historicos.append(historico)

    def listar_todos(self) -> List[HistoricoAvaliacao]:
        return self.historicos

    def buscar_por_id(self, id: int) -> Optional[HistoricoAvaliacao]:
        for h in self.historicos:
            if h.id == id:
                return h
        return None

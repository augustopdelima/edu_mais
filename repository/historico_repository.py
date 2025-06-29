from model.historico import HistoricoAvaliacao
from typing import List, Optional


class HistoricoAvaliacaoRepository:
    def __init__(self):
        self.historicos: List[HistoricoAvaliacao] = []
        print("[HistoricoAvaliacaoRepository] Inicializado")

    def salvar(self, historico: HistoricoAvaliacao) -> None:
        print(
            f"[HistoricoAvaliacaoRepository] Salvando histórico de avaliação ID {getattr(historico, 'id', 'desconhecido')}")

    def listar_todos(self) -> List[HistoricoAvaliacao]:
        print("[HistoricoAvaliacaoRepository] Listando todos os históricos de avaliação")
        return []

    def buscar_por_id(self, id: int) -> Optional[HistoricoAvaliacao]:
        print(
            f"[HistoricoAvaliacaoRepository] Buscando histórico de avaliação pelo ID: {id}")
        return None

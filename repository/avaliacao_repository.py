from typing import List, Optional
from model.avaliacao import Avaliacao


class AvaliacaoRepository:
    def __init__(self):
        self.avaliacoes: List[Avaliacao] = []

    def salvar(self, avaliacao: Avaliacao) -> None:
        self.avaliacoes.append(avaliacao)
        print(f"[AvaliacaoRepository] Avaliação com ID {avaliacao.id} salva")

    def listar_todos(self) -> List[Avaliacao]:
        print(
            f"[AvaliacaoRepository] Listando todas as avaliações ({len(self.avaliacoes)} encontradas)")
        return self.avaliacoes

    def buscar_por_id(self, id: int) -> Optional[Avaliacao]:
        print(f"[AvaliacaoRepository] Buscando avaliação pelo ID: {id}")
        for avaliacao in self.avaliacoes:
            if avaliacao.id == id:
                print(
                    f"[AvaliacaoRepository] Avaliação com ID {id} encontrada")
                return avaliacao
        print(f"[AvaliacaoRepository] Avaliação com ID {id} não encontrada")
        return None

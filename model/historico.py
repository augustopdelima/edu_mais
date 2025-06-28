from model.avaliacao import Avaliacao
from model.professor import Professor
from model.coordenador import Coordenador
from model.relatorio import Relatorio
from typing import List, Union


class HistoricoAvaliacao:
    def __init__(
        self,
        id: int,
        tipo: str,  # "professor" ou "coordenador"
        destino: Union[Professor, Coordenador],
        avaliacoes: List[Avaliacao],
        relatorio: Relatorio
    ):
        self.id = id
        self.tipo = tipo
        self.destino = destino
        self.avaliacoes = avaliacoes
        self.relatorio = relatorio

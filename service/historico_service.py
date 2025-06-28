from model.historico import HistoricoAvaliacao
from model.relatorio import Relatorio
from model.professor import Professor
from model.coordenador import Coordenador
from model.avaliacao import Avaliacao
from repository.historico_repository import HistoricoAvaliacaoRepository
from typing import List, Union


class HistoricoAvaliacaoService:
    def __init__(self, repository: HistoricoAvaliacaoRepository):
        self.repository = repository

    def gerar_historico_professor(self, professor: Professor, avaliacoes: List[Avaliacao]) -> HistoricoAvaliacao:
        indicadores = f"{len(avaliacoes)} avaliações recebidas"
        graficos = "Feedback médio: Bom"
        relatorio = Relatorio(id=1, indicadores=indicadores, graficos=graficos)

        historico = HistoricoAvaliacao(
            id=len(self.repository.listar_todos()) + 1,
            tipo="professor",
            destino=professor,
            avaliacoes=avaliacoes,
            relatorio=relatorio
        )
        self.repository.salvar(historico)
        return historico

    def gerar_historico_coordenador(self, coordenador: Coordenador, avaliacoes: List[Avaliacao]) -> HistoricoAvaliacao:
        indicadores = f"{len(avaliacoes)} avaliações no sistema"
        graficos = "Relatório de engajamento geral por disciplina"
        relatorio = Relatorio(id=2, indicadores=indicadores, graficos=graficos)

        historico = HistoricoAvaliacao(
            id=len(self.repository.listar_todos()) + 1,
            tipo="coordenador",
            destino=coordenador,
            avaliacoes=avaliacoes,
            relatorio=relatorio
        )
        self.repository.salvar(historico)
        return historico

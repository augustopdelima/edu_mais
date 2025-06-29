from service.historico_service import HistoricoAvaliacaoService
from view.historico_view import exibir_historico, listar_historicos, exibir_historico_nao_encontrado
from model.professor import Professor
from model.coordenador import Coordenador
from model.avaliacao import Avaliacao


class HistoricoAvaliacaoController:
    def __init__(self, service: HistoricoAvaliacaoService):
        self.service = service

    def gerar_para_professor(self, professor: Professor, avaliacoes: list[Avaliacao]):
        historico = self.service.gerar_historico_professor(
            professor, avaliacoes)
        exibir_historico(historico)

    def gerar_para_coordenador(self, coordenador: Coordenador, avaliacoes: list[Avaliacao]):
        historico = self.service.gerar_historico_coordenador(
            coordenador, avaliacoes)
        exibir_historico(historico)

    def listar_todos(self):
        historicos = self.service.repository.listar_todos()
        listar_historicos(historicos)

    def buscar_por_id(self, id: int):
        historico = self.service.repository.buscar_por_id(id)
        if historico:
            exibir_historico(historico)
        else:
            exibir_historico_nao_encontrado(id)

from model.historico import HistoricoAvaliacao
from typing import List


def exibir_historico(historico: HistoricoAvaliacao):
    print("\n=== Histórico de Avaliações ===")
    print(f"ID: {historico.id}")
    print(f"Tipo: {historico.tipo}")
    print(f"Destino: {historico.destino.nome}")
    print(f"Nº de Avaliações: {len(historico.avaliacoes)}")
    print(f"Indicadores: {historico.relatorio.indicadores}")
    print(f"Gráficos: {historico.relatorio.graficos}")
    print("===============================\n")


def listar_historicos(historicos: List[HistoricoAvaliacao]):
    print("=== Relatórios Gerados ===")
    for h in historicos:
        print(
            f"[{h.id}] {h.tipo.capitalize()} - {h.destino.nome} - {len(h.avaliacoes)} avaliações")
    print("===========================\n")


def exibir_historico_nao_encontrado(id: int):
    print(f"Histórico com ID {id} não encontrado.\n")
